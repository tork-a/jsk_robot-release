Name:           ros-indigo-jsk-nao-startup
Version:        0.0.10
Release:        0%{?dist}
Summary:        ROS jsk_nao_startup package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nao-interaction-msgs
Requires:       ros-indigo-naoqi-driver
Requires:       ros-indigo-roseus
Requires:       ros-indigo-rostwitter
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-naoqi-driver
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rostwitter

%description
The jsk_nao_startup package

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
* Mon Aug 17 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.10-0
- Autogenerated by Bloom

* Mon Aug 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.9-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.8-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.7-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.6-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.4-1
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.0.4-0
- Autogenerated by Bloom

