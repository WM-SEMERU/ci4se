def start(self):
    self._image_sub = rospy.Subscriber(self.topic_image_color, sensor_msgs.
        msg.Image, self._color_image_callback)
    self._depth_sub = rospy.Subscriber(self.topic_image_depth, sensor_msgs.
        msg.Image, self._depth_image_callback)
    self._camera_info_sub = rospy.Subscriber(self.topic_info_camera,
        sensor_msgs.msg.CameraInfo, self._camera_info_callback)
    timeout = 10
    try:
        rospy.loginfo('waiting to recieve a message from the Kinect')
        rospy.wait_for_message(self.topic_image_color, sensor_msgs.msg.
            Image, timeout=timeout)
        rospy.wait_for_message(self.topic_image_depth, sensor_msgs.msg.
            Image, timeout=timeout)
        rospy.wait_for_message(self.topic_info_camera, sensor_msgs.msg.
            CameraInfo, timeout=timeout)
    except rospy.ROSException as e:
        print('KINECT NOT FOUND')
        rospy.logerr('Kinect topic not found, Kinect not started')
        rospy.logerr(e)
    while self._camera_intr is None:
        time.sleep(0.1)
    self._running = True