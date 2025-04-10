%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-mecanum-drive-controller
Version:        2.44.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mecanum_drive_controller package

License:        Apache License 2.0
URL:            https://control.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-control-msgs
Requires:       ros-humble-controller-interface
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-hardware-interface
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-rcpputils
Requires:       ros-humble-realtime-tools
Requires:       ros-humble-std-srvs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-control-msgs
BuildRequires:  ros-humble-controller-interface
BuildRequires:  ros-humble-generate-parameter-library
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-hardware-interface
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-rcpputils
BuildRequires:  ros-humble-realtime-tools
BuildRequires:  ros-humble-std-srvs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-msgs
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gmock
BuildRequires:  ros-humble-controller-manager
BuildRequires:  ros-humble-hardware-interface-testing
BuildRequires:  ros-humble-ros2-control-test-assets
%endif

%description
Implementation of mecanum drive controller for 4 wheel drive.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu Apr 10 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.44.0-1
- Autogenerated by Bloom

* Mon Mar 17 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.43.0-1
- Autogenerated by Bloom

