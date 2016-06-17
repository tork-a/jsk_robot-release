Name:           ros-indigo-naoqieus
Version:        1.0.6
Release:        2%{?dist}
Summary:        ROS naoqieus package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-nao-interaction-msgs
Requires:       ros-indigo-naoqi-driver
Requires:       ros-indigo-pr2eus
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-aggregator
BuildRequires:  ros-indigo-euscollada
BuildRequires:  ros-indigo-nao-interaction-msgs
BuildRequires:  ros-indigo-naoqi-driver
BuildRequires:  ros-indigo-pr2eus
BuildRequires:  ros-indigo-rostest

%description
The naoqieus package

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
* Fri Jun 17 2016 Kei Okada <kei.okada@gmail.com> - 1.0.6-2
- Autogenerated by Bloom

* Fri Jun 17 2016 Kei Okada <kei.okada@gmail.com> - 1.0.6-1
- Autogenerated by Bloom

* Fri Jun 17 2016 Kei Okada <kei.okada@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

* Wed Apr 20 2016 Kei Okada <kei.okada@gmail.com> - 1.0.5-1
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <kei.okada@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Sat Mar 05 2016 Kei Okada <kei.okada@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Fri Feb 19 2016 Kei Okada <kei.okada@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Thu Dec 17 2015 Kei Okada <kei.okada@gmail.com> - 1.0.1-2
- Autogenerated by Bloom

* Wed Dec 16 2015 Kei Okada <kei.okada@gmail.com> - 1.0.1-1
- Autogenerated by Bloom

