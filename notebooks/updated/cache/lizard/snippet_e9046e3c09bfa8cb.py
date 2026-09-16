def maybe_add_child(self, fcoord):
    if fcoord not in self.children:
        new_position = self.position.play_move(coords.from_flat(fcoord))
        self.children[fcoord] = MCTSNode(new_position, fmove=fcoord, parent
            =self)
    return self.children[fcoord]