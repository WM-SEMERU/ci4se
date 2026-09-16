def trigger(self, source, actions, event_args):
    type = BlockType.TRIGGER
    return self.action_block(source, actions, type, event_args=event_args)