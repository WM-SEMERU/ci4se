def child(self):
    return self.stream.directory[self.child_id
        ] if self.child_id != NOSTREAM else None