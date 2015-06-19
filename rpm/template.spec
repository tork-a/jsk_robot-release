Name:           ros-indigo-pr2-base-trajectory-action
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS pr2_base_trajectory_action package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_base_trajectory_action
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-angles
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pr2-controllers-msgs
Requires:       ros-indigo-pr2-mechanism-model
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pr2-controllers-msgs
BuildRequires:  ros-indigo-pr2-mechanism-model
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-trajectory-msgs

%description
pr2_base_trajectory_action is a node that exposes and action interface to move
robot base along a trajectory.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jun 19 2015 saito <t@t.com> - 0.0.7-0
- Autogenerated by Bloom

* Fri Apr 10 2015 saito <t@t.com> - 0.0.6-0
- Autogenerated by Bloom

* Wed Apr 08 2015 saito <t@t.com> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 saito <t@t.com> - 0.0.4-1
- Autogenerated by Bloom

* Fri Jan 30 2015 saito <t@t.com> - 0.0.4-0
- Autogenerated by Bloom

