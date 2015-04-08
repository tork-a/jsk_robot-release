Name:           ros-hydro-peppereus
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS peppereus package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-diagnostic-aggregator
Requires:       ros-hydro-nao-pose
Requires:       ros-hydro-naoqi-driver
Requires:       ros-hydro-naoqi-sensors
BuildRequires:  ros-hydro-catkin

%description
The pepper_bringup package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Apr 08 2015 Kei Okada <kei.okada@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <kei.okada@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Kei Okada <kei.okada@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Kei Okada <kei.okada@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

