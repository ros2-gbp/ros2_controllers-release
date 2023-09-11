%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-ros2-controllers-test-nodes
Version:        3.15.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers_test_nodes package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-rclpy
Requires:       ros-iron-std-msgs
Requires:       ros-iron-trajectory-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-std-msgs
BuildRequires:  ros-iron-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Mon Sep 11 2023 Denis Štogl <denis@stoglrobotics.de> - 3.15.0-1
- Autogenerated by Bloom

* Wed Aug 16 2023 Denis Štogl <denis@stoglrobotics.de> - 3.14.0-1
- Autogenerated by Bloom

* Fri Aug 04 2023 Denis Štogl <denis@stoglrobotics.de> - 3.13.0-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Denis Štogl <denis@stoglrobotics.de> - 3.12.0-1
- Autogenerated by Bloom

* Sat Jun 24 2023 Denis Štogl <denis@stoglrobotics.de> - 3.11.0-1
- Autogenerated by Bloom

* Tue Jun 06 2023 Denis Štogl <denis@stoglrobotics.de> - 3.10.1-1
- Autogenerated by Bloom

* Sun Jun 04 2023 Denis Štogl <denis@stoglrobotics.de> - 3.10.0-1
- Autogenerated by Bloom

* Sun May 28 2023 Denis Štogl <denis@stoglrobotics.de> - 3.9.0-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Denis Štogl <denis@stoglrobotics.de> - 3.5.0-2
- Autogenerated by Bloom

* Fri Apr 14 2023 Denis Štogl <denis@stoglrobotics.de> - 3.5.0-1
- Autogenerated by Bloom

* Sun Apr 02 2023 Denis Štogl <denis@stoglrobotics.de> - 3.4.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Denis Štogl <denis@stoglrobotics.de> - 3.3.0-2
- Autogenerated by Bloom

