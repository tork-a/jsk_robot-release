Name:           ros-hydro-jsk-pr2-startup
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS jsk_pr2_startup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_pr2_startup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-dwa-local-planner
Requires:       ros-hydro-jsk-interactive-marker
Requires:       ros-hydro-jsk-network-tools
Requires:       ros-hydro-jsk-robot-startup
Requires:       ros-hydro-pr2-gripper-sensor-action
Requires:       ros-hydro-pr2-mannequin-mode
BuildRequires:  ros-hydro-amcl
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-dwa-local-planner
BuildRequires:  ros-hydro-dynamic-tf-publisher
BuildRequires:  ros-hydro-image-view2
BuildRequires:  ros-hydro-imagesift
BuildRequires:  ros-hydro-jsk-interactive-marker
BuildRequires:  ros-hydro-jsk-network-tools
BuildRequires:  ros-hydro-jsk-pcl-ros
BuildRequires:  ros-hydro-jsk-perception
BuildRequires:  ros-hydro-jsk-robot-startup
BuildRequires:  ros-hydro-jsk-topic-tools
BuildRequires:  ros-hydro-map-server
BuildRequires:  ros-hydro-mjpeg-server
BuildRequires:  ros-hydro-move-base
BuildRequires:  ros-hydro-move-base-msgs
BuildRequires:  ros-hydro-openni-camera
BuildRequires:  ros-hydro-pr2-base-trajectory-action
BuildRequires:  ros-hydro-pr2-gripper-sensor-action
BuildRequires:  ros-hydro-pr2-mannequin-mode
BuildRequires:  ros-hydro-resized-image-transport
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rostwitter
BuildRequires:  ros-hydro-rqt-gui
BuildRequires:  ros-hydro-rqt-gui-py
BuildRequires:  ros-hydro-rqt-py-common
BuildRequires:  ros-hydro-sound-play
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf2
BuildRequires:  ros-hydro-tf2-ros
BuildRequires:  ros-hydro-topic-tools
BuildRequires:  ros-hydro-voice-text

%description
jsk_pr2_startup

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
* Fri Apr 10 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.6-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.3-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.2-0
- Autogenerated by Bloom

* Thu Dec 25 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.1-1
- Autogenerated by Bloom

* Thu Dec 25 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.1-0
- Autogenerated by Bloom

