def nack(self, delivery_tag, multiple=False, requeue=False):
    args = Writer()
    args.write_longlong(delivery_tag).write_bits(multiple, requeue)
    self.send_frame(MethodFrame(self.channel_id, 60, 120, args))