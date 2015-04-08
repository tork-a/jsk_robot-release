Name:           ros-hydro-jsk-baxter-startup
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS jsk_baxter_startup package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-baxter-core-msgs
Requires:       ros-hydro-baxter-description
Requires:       ros-hydro-baxter-examples
Requires:       ros-hydro-baxter-interface
Requires:       ros-hydro-baxter-tools
Requires:       ros-hydro-checkerboard-detector
Requires:       ros-hydro-dynamic-tf-publisher
Requires:       ros-hydro-image-view
Requires:       ros-hydro-joy
Requires:       ros-hydro-openni-launch
Requires:       ros-hydro-roseus
Requires:       ros-hydro-rostwitter
Requires:       ros-hydro-sound-play
Requires:       ros-hydro-topic-tools
BuildRequires:  ros-hydro-baxter-core-msgs
BuildRequires:  ros-hydro-baxter-description
BuildRequires:  ros-hydro-baxter-examples
BuildRequires:  ros-hydro-baxter-interface
BuildRequires:  ros-hydro-baxter-tools
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-checkerboard-detector
BuildRequires:  ros-hydro-dynamic-tf-publisher
BuildRequires:  ros-hydro-image-view
BuildRequires:  ros-hydro-joy
BuildRequires:  ros-hydro-openni-launch
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rostwitter
BuildRequires:  ros-hydro-sound-play
BuildRequires:  ros-hydro-topic-tools

%description
The jsk_baxter_startup package

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
* Wed Apr 08 2015 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.3-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.2-0
- Autogenerated by Bloom

* Thu Dec 25 2014 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.1-1
- Autogenerated by Bloom

* Thu Dec 25 2014 Yuto Inagaki <inagaki@jsk.imi.i.u-tokyo.ac.jp> - 0.0.1-0
- Autogenerated by Bloom

