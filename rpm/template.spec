%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-joint-trajectory-controller
Version:        1.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS joint_trajectory_controller package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-angles
Requires:       ros-galactic-control-msgs
Requires:       ros-galactic-controller-interface
Requires:       ros-galactic-hardware-interface
Requires:       ros-galactic-pluginlib
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-lifecycle
Requires:       ros-galactic-realtime-tools
Requires:       ros-galactic-trajectory-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-angles
BuildRequires:  ros-galactic-control-msgs
BuildRequires:  ros-galactic-controller-interface
BuildRequires:  ros-galactic-controller-manager
BuildRequires:  ros-galactic-hardware-interface
BuildRequires:  ros-galactic-pluginlib
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-lifecycle
BuildRequires:  ros-galactic-realtime-tools
BuildRequires:  ros-galactic-ros2-control-test-assets
BuildRequires:  ros-galactic-trajectory-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Controller for executing joint-space trajectories on a group of joints

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Jan 11 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.3.0-1
- Autogenerated by Bloom

* Wed Dec 29 2021 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.2.0-1
- Autogenerated by Bloom

* Mon Oct 25 2021 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.1.0-1
- Autogenerated by Bloom

* Thu Sep 30 2021 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.0.0-1
- Autogenerated by Bloom

