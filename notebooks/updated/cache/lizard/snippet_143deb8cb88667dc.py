def put_collisions(self, block_id, collisions):
    self.collisions[block_id] = copy.deepcopy(collisions)