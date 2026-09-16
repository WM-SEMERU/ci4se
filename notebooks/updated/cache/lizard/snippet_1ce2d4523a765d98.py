def delete(self, value, key):
    if self is NULL:
        raise KeyError(value)
    direction = cmp(key(value), key(self.value))
    if direction < 0:
        if (not self.left.red and self.left is not NULL and not self.left.
            left.red):
            self = self.move_red_left()
        left = self.left.delete(value, key)
        self = self._replace(left=left)
    else:
        if self.left.red:
            self = self.rotate_right()
        if direction == 0 and self.right is NULL:
            return NULL
        if (not self.right.red and self.right is not NULL and not self.
            right.left.red):
            self = self.move_red_right()
        if direction > 0:
            right = self.right.delete(value, key)
            self = self._replace(right=right)
        else:
            rnode = self.right
            while rnode is not NULL:
                rnode = rnode.left
            right, replacement = self.right.delete_min()
            self = self._replace(value=replacement, right=right)
    return self.balance()