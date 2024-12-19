// Copyright (c) 2023, Stogl Robotics Consulting UG (haftungsbeschränkt)
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "test_tricycle_steering_controller.hpp"

#include <memory>
#include <string>
#include <vector>

class TricycleSteeringControllerTest
: public TricycleSteeringControllerFixture<TestableTricycleSteeringController>
{
};

TEST_F(TricycleSteeringControllerTest, all_parameters_set_configure_success)
{
  SetUpController();

  ASSERT_EQ(controller_->on_configure(rclcpp_lifecycle::State()), NODE_SUCCESS);

  ASSERT_THAT(
    controller_->params_.rear_wheels_names,
    testing::ElementsAreArray(rear_wheels_preceeding_names_));
  ASSERT_THAT(
    controller_->params_.front_wheels_names,
    testing::ElementsAreArray(front_wheels_preceeding_names_));
  ASSERT_EQ(controller_->params_.front_steering, front_steering_);
  ASSERT_EQ(controller_->params_.open_loop, open_loop_);
  ASSERT_EQ(controller_->params_.velocity_rolling_window_size, velocity_rolling_window_size_);
  ASSERT_EQ(controller_->params_.position_feedback, position_feedback_);
  ASSERT_EQ(controller_->tricycle_params_.wheelbase, wheelbase_);
  ASSERT_EQ(controller_->tricycle_params_.front_wheels_radius, front_wheels_radius_);
  ASSERT_EQ(controller_->tricycle_params_.rear_wheels_radius, rear_wheels_radius_);
  ASSERT_EQ(controller_->tricycle_params_.wheel_track, wheel_track_);
}

TEST_F(TricycleSteeringControllerTest, check_exported_interfaces)
{
  SetUpController();

  ASSERT_EQ(controller_->on_configure(rclcpp_lifecycle::State()), NODE_SUCCESS);

  auto cmd_if_conf = controller_->command_interface_configuration();
  ASSERT_EQ(cmd_if_conf.names.size(), joint_command_values_.size());
  EXPECT_EQ(
    cmd_if_conf.names[CMD_TRACTION_RIGHT_WHEEL],
    preceeding_prefix_ + "/" + rear_wheels_names_[0] + "/" + traction_interface_name_);
  EXPECT_EQ(
    cmd_if_conf.names[CMD_TRACTION_LEFT_WHEEL],
    preceeding_prefix_ + "/" + rear_wheels_names_[1] + "/" + traction_interface_name_);
  EXPECT_EQ(
    cmd_if_conf.names[CMD_STEER_WHEEL],
    preceeding_prefix_ + "/" + front_wheels_names_[0] + "/" + steering_interface_name_);
  EXPECT_EQ(cmd_if_conf.type, controller_interface::interface_configuration_type::INDIVIDUAL);

  auto state_if_conf = controller_->state_interface_configuration();
  ASSERT_EQ(state_if_conf.names.size(), joint_state_values_.size());
  EXPECT_EQ(
    state_if_conf.names[STATE_TRACTION_RIGHT_WHEEL],
    controller_->rear_wheels_state_names_[0] + "/" + traction_interface_name_);
  EXPECT_EQ(
    state_if_conf.names[STATE_TRACTION_LEFT_WHEEL],
    controller_->rear_wheels_state_names_[1] + "/" + traction_interface_name_);
  EXPECT_EQ(
    state_if_conf.names[STATE_STEER_AXIS],
    controller_->front_wheels_state_names_[0] + "/" + steering_interface_name_);
  EXPECT_EQ(state_if_conf.type, controller_interface::interface_configuration_type::INDIVIDUAL);

  // check ref itfs
  auto ref_if_conf = controller_->export_reference_interfaces();
  ASSERT_EQ(ref_if_conf.size(), joint_reference_interfaces_.size());
  for (size_t i = 0; i < joint_reference_interfaces_.size(); ++i)
  {
    const std::string ref_itf_name =
      std::string(controller_->get_node()->get_name()) + "/" + joint_reference_interfaces_[i];
    EXPECT_EQ(ref_if_conf[i]->get_name(), ref_itf_name);
    EXPECT_EQ(ref_if_conf[i]->get_prefix_name(), controller_->get_node()->get_name());
    EXPECT_EQ(ref_if_conf[i]->get_interface_name(), joint_reference_interfaces_[i]);
  }
}

int main(int argc, char ** argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  rclcpp::init(argc, argv);
  int result = RUN_ALL_TESTS();
  rclcpp::shutdown();
  return result;
}
