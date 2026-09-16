def list_to_pose(poselist, frame_id='', stamp=rospy.Time(0)):
    p = PoseStamped()
    p.header.frame_id = frame_id
    p.header.stamp = stamp
    p.pose.position.x = poselist[0][0]
    p.pose.position.y = poselist[0][1]
    p.pose.position.z = poselist[0][2]
    p.pose.orientation.x = poselist[1][0]
    p.pose.orientation.y = poselist[1][1]
    p.pose.orientation.z = poselist[1][2]
    p.pose.orientation.w = poselist[1][3]
    return p