def set_partition(self, partition):
    assert len(partition) == self.numgrp
    self.partition, self.prev_partition = partition, self.partition