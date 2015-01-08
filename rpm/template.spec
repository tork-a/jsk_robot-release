Name:           ros-hydro-jsk-pr2-calibration
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS jsk_pr2_calibration package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-euscollada
Requires:       ros-hydro-pr2-calibration-launch
Requires:       ros-hydro-pr2-description
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-euscollada
BuildRequires:  ros-hydro-pr2-calibration-launch
BuildRequires:  ros-hydro-pr2-description

%description
The jsk_pr2_calibration package

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
* Thu Jan 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.2-0
- Autogenerated by Bloom

* Thu Dec 25 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.1-1
- Autogenerated by Bloom

* Thu Dec 25 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.1-0
- Autogenerated by Bloom

