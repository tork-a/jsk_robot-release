Name:           ros-indigo-roseus-remote
Version:        0.0.11
Release:        0%{?dist}
Summary:        ROS roseus_remote package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-jsk-network-tools
Requires:       ros-indigo-roseus
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-jsk-network-tools
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-std-msgs

%description
The jskeus_remote package

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
* Tue Sep 01 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.11-0
- Autogenerated by Bloom

* Mon Aug 17 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.10-1
- Autogenerated by Bloom

* Mon Aug 17 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.10-0
- Autogenerated by Bloom

* Mon Aug 03 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.9-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.8-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.7-0
- Autogenerated by Bloom

