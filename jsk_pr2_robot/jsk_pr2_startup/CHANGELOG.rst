^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package jsk_pr2_startup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.3 (2015-01-09)
------------------

0.0.2 (2015-01-08)
------------------
* add install commands to cmake
* [jsk_pr2_startup] Disable collider node, it's out of date
* Merge pull request #232 from garaemon/rename-hydro-recognition
  [jsk_pr2_startup] rename hydro_recognition.launch to people_detection.launch and start it up default
* [jsk_pr2_startup] Remove torso_lift_link from self filtering of
  tilt laser to avoid too much filtering of points. And update padding
  of shoulder links to remove veiling noise
* [jsk_pr2_startup] rename hydro_recognition.launch to people_detection.launch
  and start it up in default.
* Merge pull request #230 from garaemon/move-image-processing-to-c2
  [jsk_pr2_startup] Move several image processing to c2 to avoid heavy network communication between c1 and c2
* [jsk_pr2_startup] Move several image processing to c2 to avoid heavy
  network communication between c1 and c2
* [jsk_pr2_startup] Throttle before applying image_view2 to decrease
  CPU load
* use robot-actions.l
* Fix parameter namespace to slow down pr2_gripper_sensor_action
* Use longer priod to check openni soundness
* use rostwitter and python_twoauth
* Contributors: Kei Okada, Ryohei Ueda, Yusuke Furuta

0.0.1 (2014-12-25)
------------------
* Restarting kinect paranoiac
  1) usb reset
  2) kill nodelet manager
  3) kill child processing
  4) restart openni.launch (hardcoded!)
* Add rviz_mouse_point_to_tablet.py to pr2.launch
* Use larger value to detect gound object by PR2 to avoid small noises
* Add sound when launching pr2.launch
* kill nodelet manager and processes rather than killing openni/driver
* Say something at the end of pr2.launch
* Use low framerate for gripper sensors to avoid high load
* move twitter related program to robot_common from jsk_pr2_startup
* modify launch file for gazebo
* add yaml file for gazebo
* delete LaserScanIntensityFilter
* modify sensors_kinect and add sensors
* move pr2 related package under jsk_pr2_robot
* Contributors: Ryohei Ueda, Yuto Inagaki, Yusuke Furuta
