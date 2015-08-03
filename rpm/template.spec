Name:           ros-indigo-jsk-pr2-startup
Version:        0.0.9
Release:        0%{?dist}
Summary:        ROS jsk_pr2_startup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_pr2_startup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dwa-local-planner
Requires:       ros-indigo-jsk-interactive-marker
Requires:       ros-indigo-jsk-network-tools
Requires:       ros-indigo-jsk-robot-startup
Requires:       ros-indigo-pr2-gripper-sensor-action
Requires:       ros-indigo-pr2-mannequin-mode
BuildRequires:  ros-indigo-amcl
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dwa-local-planner
BuildRequires:  ros-indigo-dynamic-tf-publisher
BuildRequires:  ros-indigo-face-detector
BuildRequires:  ros-indigo-image-view2
BuildRequires:  ros-indigo-imagesift
BuildRequires:  ros-indigo-jsk-interactive-marker
BuildRequires:  ros-indigo-jsk-network-tools
BuildRequires:  ros-indigo-jsk-pcl-ros
BuildRequires:  ros-indigo-jsk-perception
BuildRequires:  ros-indigo-jsk-robot-startup
BuildRequires:  ros-indigo-jsk-topic-tools
BuildRequires:  ros-indigo-leg-detector
BuildRequires:  ros-indigo-map-server
BuildRequires:  ros-indigo-mjpeg-server
BuildRequires:  ros-indigo-move-base
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-openni-camera
BuildRequires:  ros-indigo-people-velocity-tracker
BuildRequires:  ros-indigo-pr2-base-trajectory-action
BuildRequires:  ros-indigo-pr2-gripper-sensor-action
BuildRequires:  ros-indigo-pr2-mannequin-mode
BuildRequires:  ros-indigo-resized-image-transport
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostwitter
BuildRequires:  ros-indigo-rqt-gui
BuildRequires:  ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-rqt-py-common
BuildRequires:  ros-indigo-sound-play
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-topic-tools
BuildRequires:  ros-indigo-voice-text

%description
jsk_pr2_startup

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
* Mon Aug 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.9-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.8-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.7-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.6-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.5-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.4-1
- Autogenerated by Bloom

* Fri Jan 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.4-0
- Autogenerated by Bloom

