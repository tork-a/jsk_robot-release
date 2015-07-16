Name:           ros-hydro-roseus-remote
Version:        0.0.8
Release:        0%{?dist}
Summary:        ROS roseus_remote package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-jsk-network-tools
Requires:       ros-hydro-roseus
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-jsk-network-tools
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-std-msgs

%description
The jskeus_remote package

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
* Thu Jul 16 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.8-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 0.0.7-0
- Autogenerated by Bloom

