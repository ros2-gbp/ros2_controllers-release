%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-tricycle-steering-controller
Version:        3.26.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tricycle_steering_controller package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-backward-ros
Requires:       ros-iron-control-msgs
Requires:       ros-iron-controller-interface
Requires:       ros-iron-hardware-interface
Requires:       ros-iron-pluginlib
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rclcpp-lifecycle
Requires:       ros-iron-std-srvs
Requires:       ros-iron-steering-controllers-library
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-backward-ros
BuildRequires:  ros-iron-control-msgs
BuildRequires:  ros-iron-controller-interface
BuildRequires:  ros-iron-generate-parameter-library
BuildRequires:  ros-iron-hardware-interface
BuildRequires:  ros-iron-pluginlib
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rclcpp-lifecycle
BuildRequires:  ros-iron-std-srvs
BuildRequires:  ros-iron-steering-controllers-library
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-gmock
BuildRequires:  ros-iron-controller-manager
BuildRequires:  ros-iron-hardware-interface-testing
BuildRequires:  ros-iron-ros2-control-test-assets
%endif

%description
Steering controller with tricycle kinematics. Rear fixed wheels are powering the
vehicle and front wheel is steering.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Aug 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.26.2-1
- Autogenerated by Bloom

* Wed Aug 14 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.26.1-1
- Autogenerated by Bloom

* Wed Jul 24 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.26.0-1
- Autogenerated by Bloom

* Tue Jul 09 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.25.0-1
- Autogenerated by Bloom

* Tue May 14 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.24.0-1
- Autogenerated by Bloom

* Tue Apr 30 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.23.0-1
- Autogenerated by Bloom

* Mon Feb 12 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.22.0-1
- Autogenerated by Bloom

* Sat Jan 20 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.21.0-1
- Autogenerated by Bloom

* Thu Jan 11 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.20.2-1
- Autogenerated by Bloom

* Mon Jan 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.20.1-1
- Autogenerated by Bloom

* Wed Jan 03 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.20.0-1
- Autogenerated by Bloom

* Tue Dec 12 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.19.2-1
- Autogenerated by Bloom

* Tue Dec 05 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.19.1-1
- Autogenerated by Bloom

* Fri Dec 01 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.19.0-1
- Autogenerated by Bloom

* Tue Nov 21 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.18.0-1
- Autogenerated by Bloom

* Tue Oct 31 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.17.0-1
- Autogenerated by Bloom

* Wed Sep 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.16.0-1
- Autogenerated by Bloom

* Mon Sep 11 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.15.0-1
- Autogenerated by Bloom

* Wed Aug 16 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.14.0-1
- Autogenerated by Bloom

* Fri Aug 04 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.13.0-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.12.0-1
- Autogenerated by Bloom

* Sat Jun 24 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.11.0-1
- Autogenerated by Bloom

* Tue Jun 06 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.10.1-1
- Autogenerated by Bloom

* Sun Jun 04 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.10.0-1
- Autogenerated by Bloom

* Sun May 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.9.0-1
- Autogenerated by Bloom

