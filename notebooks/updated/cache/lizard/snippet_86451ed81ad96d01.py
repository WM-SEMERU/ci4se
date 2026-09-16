def pop(self):
    stack = getattr(self._local, 'stack', None)
    if stack is None:
        return None
    elif len(stack) == 1:
        release_local(self._local)
        return stack[-1]
    else:
        return stack.pop()