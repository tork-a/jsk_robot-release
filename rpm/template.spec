Name:           ros-indigo-jsk-robot-startup
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS jsk_robot_startup package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-mongodb-store
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-mongodb-store
BuildRequires:  ros-indigo-pr2-mechanism-controllers
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs

%description
The jsk_robot_startup package

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
* Fri Jun 19 2015 inagaki <inagaki@todo.todo> - 0.0.7-0
- Autogenerated by Bloom

* Fri Apr 10 2015 inagaki <inagaki@todo.todo> - 0.0.6-0
- Autogenerated by Bloom

* Wed Apr 08 2015 inagaki <inagaki@todo.todo> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 inagaki <inagaki@todo.todo> - 0.0.4-1
- Autogenerated by Bloom

* Fri Jan 30 2015 inagaki <inagaki@todo.todo> - 0.0.4-0
- Autogenerated by Bloom

