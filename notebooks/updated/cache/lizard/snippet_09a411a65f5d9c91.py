def blocks_to_mark_complete_on_view(self, blocks):
    blocks = {block for block in blocks if self.
        can_mark_block_complete_on_view(block)}
    completions = self.get_completions({block.location for block in blocks})
    return {block for block in blocks if completions.get(block.location, 0) <
        1.0}