def change_base(state, point=Point(0, 0, 0), src=ROOT, dst=ROOT):

    def fold(objects):
        return functools.reduce(lambda a, b: a.dot(b), [state[key].
            transform for key in objects], np.identity(4))
    up, down = ascend(state, src), list(reversed(ascend(state, dst)))
    root = [n1 for n1, n2 in zip(reversed(up), down) if n1 is n2].pop()
    up = list(itertools.takewhile(lambda node: node is not root, up))
    down = list(itertools.dropwhile(lambda node: node is not root, down))[1:]
    point_in_root = inv(fold(up)).dot((*point, 1))
    return fold(down).dot(point_in_root)[:-1]