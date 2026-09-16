def pose_to_list(pose):
    if type(pose) == geometry_msgs.msg.PoseStamped:
        return [[pose.pose.position.x, pose.pose.position.y, pose.pose.
            position.z], [pose.pose.orientation.x, pose.pose.orientation.y,
            pose.pose.orientation.z, pose.pose.orientation.w]]
    elif type(pose) == geometry_msgs.msg.Pose:
        return [[pose.position.x, pose.position.y, pose.position.z], [pose.
            orientation.x, pose.orientation.y, pose.orientation.z, pose.
            orientation.w]]
    else:
        raise Exception('pose_to_list: parameter of type %s unexpected',
            str(type(pose)))