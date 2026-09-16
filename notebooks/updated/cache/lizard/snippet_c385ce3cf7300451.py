def handle_snapshot(self, msg):
    logging.debug('Sending state snapshot request')
    identity = msg[0]
    self.snapshot.send_multipart([identity] + msgs.MessageBuilder.
        mainswitch_state(self.sequence_number, self.app.state.mainswitch))
    self.snapshot.send_multipart([identity] + msgs.MessageBuilder.
        brightness(self.sequence_number, self.app.state.brightness))
    for animation_id, anim in enumerate(self.app.state.animationClasses):
        self.snapshot.send_multipart([identity] + msgs.MessageBuilder.
            animation_add(self.sequence_number, animation_id, anim.name))
    for scene_id, scene in self.app.state.scenes.items():
        self.snapshot.send_multipart([identity] + msgs.MessageBuilder.
            scene_add(self.sequence_number, scene_id, scene.animation_id,
            scene.name, scene.color, scene.velocity, scene.config))
    self.snapshot.send_multipart([identity] + msgs.MessageBuilder.
        scene_active(self.sequence_number, 0 if self.app.state.
        activeSceneId is None else self.app.state.activeSceneId))