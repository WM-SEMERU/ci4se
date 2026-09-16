async def move_camera_spatial(self, position: Union[Point2, Point3]):
    from s2clientprotocol import spatial_pb2 as spatial_pb
    assert isinstance(position, (Point2, Point3))
    action = sc_pb.Action(action_render=spatial_pb.ActionSpatial(
        camera_move=spatial_pb.ActionSpatialCameraMove(center_minimap=
        common_pb.PointI(x=position.x, y=position.y))))
    await self._execute(action=sc_pb.RequestAction(actions=[action]))