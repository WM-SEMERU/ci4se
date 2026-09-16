def publish_scene_color(self, scene_id, color):
    self.sequence_number += 1
    self.publisher.send_multipart(msgs.MessageBuilder.scene_color(self.
        sequence_number, scene_id, color))
    return self.sequence_number