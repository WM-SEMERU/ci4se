def set_scene_velocity(self, scene_id, velocity):
    if not scene_id in self.state.scenes:
        err_msg = (
            'Requested to set velocity on scene {sceneNum}, which does not exist'
            .format(sceneNum=scene_id))
        logging.info(err_msg)
        return False, 0, err_msg
    self.state.scenes[scene_id] = self.state.scenes[scene_id]._replace(velocity
        =velocity)
    sequence_number = self.zmq_publisher.publish_scene_velocity(scene_id,
        velocity)
    logging.debug('set velocity on scene {sceneNum}'.format(sceneNum=scene_id))
    if scene_id == self.state.activeSceneId:
        self.state.activeAnimation.set_velocity(velocity)
        self._do_next_frame()
    return True, sequence_number, 'OK'