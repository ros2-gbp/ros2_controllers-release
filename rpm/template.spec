%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2-controllers-test-nodes
Version:        4.18.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers_test_nodes package

License:        Apache License 2.0
URL:            https://control.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rclpy
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-trajectory-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-launch-testing-ros
%endif

%description
Demo nodes for showing and testing functionalities of the ros2_control
framework.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Dec 19 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.18.0-1
- Autogenerated by Bloom

* Sat Dec 07 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.17.0-1
- Autogenerated by Bloom

* Fri Nov 08 2024 Denis Štogl <denis@stoglrobotics.de> - 4.16.0-1
- Autogenerated by Bloom

* Mon Oct 07 2024 Denis Štogl <denis@stoglrobotics.de> - 4.15.0-1
- Autogenerated by Bloom

* Wed Sep 11 2024 Denis Štogl <denis@stoglrobotics.de> - 4.14.0-1
- Autogenerated by Bloom

* Thu Aug 22 2024 Denis Štogl <denis@stoglrobotics.de> - 4.13.0-1
- Autogenerated by Bloom

* Wed Aug 14 2024 Denis Štogl <denis@stoglrobotics.de> - 4.12.1-1
- Autogenerated by Bloom

* Tue Jul 23 2024 Denis Štogl <denis@stoglrobotics.de> - 4.12.0-1
- Autogenerated by Bloom

* Tue Jul 09 2024 Denis Štogl <denis@stoglrobotics.de> - 4.11.0-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Denis Štogl <denis@stoglrobotics.de> - 4.10.0-1
- Autogenerated by Bloom

* Wed Jun 05 2024 Denis Štogl <denis@stoglrobotics.de> - 4.9.0-1
- Autogenerated by Bloom

* Tue May 14 2024 Denis Štogl <denis@stoglrobotics.de> - 4.8.0-1
- Autogenerated by Bloom

* Fri Mar 22 2024 Denis Štogl <denis@stoglrobotics.de> - 4.7.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Denis Štogl <denis@stoglrobotics.de> - 4.6.0-2
- Autogenerated by Bloom

