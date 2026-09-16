def get_item(self, sequence_id, position):
    return self.from_record(self.get_record(sequence_id, position))