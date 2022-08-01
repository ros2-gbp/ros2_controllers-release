// Copyright 2020 PAL Robotics S.L.
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

#ifndef FORWARD_COMMAND_CONTROLLER__FORWARD_COMMAND_CONTROLLER_HPP_
#define FORWARD_COMMAND_CONTROLLER__FORWARD_COMMAND_CONTROLLER_HPP_

#include <string>
#include <vector>

#include "forward_command_controller/forward_controllers_base.hpp"
#include "forward_command_controller/visibility_control.h"

namespace forward_command_controller
{
/**
 * \brief Forward command controller for a set of joints.
 *
 * This class forwards the command signal down to a set of joints on the specified interface.
 *
 * \param joints Names of the joints to control.
 * \param interface_name Name of the interface to command.
 *
 * Subscribes to:
 * - \b commands (std_msgs::msg::Float64MultiArray) : The commands to apply.
 */
class ForwardCommandController : public ForwardControllersBase
{
public:
  FORWARD_COMMAND_CONTROLLER_PUBLIC
  ForwardCommandController();

protected:
  void declare_parameters() override;
  controller_interface::CallbackReturn read_parameters() override;

  std::vector<std::string> joint_names_;
  std::string interface_name_;
};

}  // namespace forward_command_controller

#endif  // FORWARD_COMMAND_CONTROLLER__FORWARD_COMMAND_CONTROLLER_HPP_
