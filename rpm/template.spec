%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-gpio-controllers
Version:        4.19.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gpio_controllers package

License:        Apache License 2.0
URL:            https://control.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-control-msgs
Requires:       ros-jazzy-controller-interface
Requires:       ros-jazzy-generate-parameter-library
Requires:       ros-jazzy-hardware-interface
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-lifecycle
Requires:       ros-jazzy-realtime-tools
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-control-msgs
BuildRequires:  ros-jazzy-controller-interface
BuildRequires:  ros-jazzy-generate-parameter-library
BuildRequires:  ros-jazzy-hardware-interface
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-lifecycle
BuildRequires:  ros-jazzy-realtime-tools
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gmock
BuildRequires:  ros-jazzy-controller-manager
BuildRequires:  ros-jazzy-hardware-interface-testing
BuildRequires:  ros-jazzy-ros2-control-test-assets
%endif

%description
Controllers to interact with gpios.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon Jan 13 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.19.0-1
- Autogenerated by Bloom

* Thu Dec 19 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.18.0-1
- Autogenerated by Bloom

* Sat Dec 07 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.17.0-1
- Autogenerated by Bloom

