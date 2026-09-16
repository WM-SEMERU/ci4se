def jump_to(self, *, iterator_type, sequence_number=None):
    self.iterator_id = self.session.get_shard_iterator(stream_arn=self.
        stream_arn, shard_id=self.shard_id, iterator_type=iterator_type,
        sequence_number=sequence_number)
    self.iterator_type = iterator_type
    self.sequence_number = sequence_number
    self.empty_responses = 0