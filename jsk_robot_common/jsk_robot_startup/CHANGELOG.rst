^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package jsk_robot_startup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.10 (2015-08-16)
-------------------
* [jsk_robot_startup] fix camera namespace openni -> kinect_head
* [jsk_robot_startup] Add odometry accuracy parameters for gmapping
* [jsk_robot_startup] Add scripts to reset slam and heightmap according to /odom_init_trigger
  topic
* [jsk_robot_startup] Add gmapping.rviz for gmapping.launch
* [jsk_robot_startup] Add delta/particle/minimum_score parameters for gmapping
* [jsk_robot_startup] use param "robot/name"
  [jsk_pr2_startup] use daemon mongod
* [jsk_robot_startup] Add rate param to modify tf publish rate and set 10.0 as defalut
* add run depend for mapping
* [jsk_robot_startup] Enable inf value in pointcloud_to_laserscan to prevent robot from obtaining wrong obstacles
* Contributors: Yuki Furuta, Ryohei Ueda, Yu Ohara, Iori Kumagai

0.0.9 (2015-08-03)
------------------
* [jsk_robot_startup] Modify node name of gmapping and pointcloud_to_laserscan
* [jsk_robot_startup] Add respawn to gmapping
* [jsk_robot_startup] Add angle_max and angle_min arguments to determine horizontal scan range
* [jsk_robot_startup] Fix x, y and yaw of pointcloud_toscan_base to parent, roll and pitch to /odom
* [jsk_robot_startup] Fix roll and pitch angle of cosntant height frame same as /odom
* [jsk_robot_startup] Add gmapping to run_depend
* [jsk_robot_startup] Add scripts and launch files for gmapping
* [jsk_robot_startup] support daemon mode mongod; enable replication to jsk robot-database
* Contributors: Iori Kumagai, Yuki Furuta

0.0.8 (2015-07-16)
------------------

0.0.7 (2015-06-11)
------------------

0.0.6 (2015-04-10)
------------------

0.0.5 (2015-04-08)
------------------
* [jsk_baxter_startup] update to add position diff paramter for tweet
* [jsk_baxter_startup] modify to prevent baxter.launch fail
* [jsk_robot_startup/package.xml: add diagnostic_msgs, pr2_mechanism_controllers, sensor_msgs to build dependencies
* [sk_robot_startup/CMakeLists.txt] update to set permission for installed script files
* [jsk_robot_startup] modfiy CMakeLists.txt to install jsk_robot_startup correctly
* [jsk_robot_startup/lifelog/active_user.l] repair tweet lifelog
* [jsk_robot_startup/lifelog/mongodb.launch] fix typo of option in launch
* [jsk_robot_startup/lifelog/mongodb.launch: add mongodb launch; mongod kill watcher
* Contributors: Yuki Furuta, Yuto Inagaki

0.0.4 (2015-01-30)
------------------

0.0.3 (2015-01-09)
------------------

0.0.2 (2015-01-08)
------------------

0.0.1 (2014-12-25)
------------------
* check joint state and set movep for odom disable robot
* Add sound when launching pr2.launch
* Say something at the end of pr2.launch
* move twitter related program to robot_common from jsk_pr2_startup
* add ros-info
* robot time signal
* add tweet.l, see jsk_nao_startup.launch for example
* repiar mongodb.launch
* repair mongodb.launch and add param
* add jsk_robot_common/jsk_robot_startup
* Contributors: Kanae Kochigami, Ryohei Ueda, Yuto Inagaki, Yusuke Furuta
