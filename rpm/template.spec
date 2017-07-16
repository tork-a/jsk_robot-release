Name:           ros-indigo-jsk-robot-utils
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS jsk_robot_utils package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-jsk-network-tools
Requires:       ros-indigo-pr2eus
Requires:       ros-indigo-roseus
Requires:       ros-indigo-rostest
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-joint-state-publisher
BuildRequires:  ros-indigo-jsk-network-tools
BuildRequires:  ros-indigo-pr2eus
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rostest

%description
jsk_robot_utils

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sun Jul 16 2017 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Fri Jun 17 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.6-2
- Autogenerated by Bloom

* Fri Jun 17 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.6-1
- Autogenerated by Bloom

* Fri Jun 17 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.6-0
- Autogenerated by Bloom

* Wed Apr 20 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.5-1
- Autogenerated by Bloom

* Mon Mar 21 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.4-0
- Autogenerated by Bloom

* Sat Mar 05 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.3-0
- Autogenerated by Bloom

* Fri Feb 19 2016 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.2-0
- Autogenerated by Bloom

* Thu Dec 17 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.1-2
- Autogenerated by Bloom

* Wed Dec 16 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 1.0.1-1
- Autogenerated by Bloom

* Tue Sep 01 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 0.0.11-0
- Autogenerated by Bloom

* Mon Aug 17 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 0.0.10-1
- Autogenerated by Bloom

* Mon Aug 17 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 0.0.10-0
- Autogenerated by Bloom

* Mon Aug 03 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 0.0.9-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Ryohei Ueda <ueda@jsk.imi.i.u-tokyo.ac.jp> - 0.0.8-0
- Autogenerated by Bloom

