def calc_cost(self, node_a, node_b):
    if node_b.x - node_a.x == 0 or node_b.y - node_a.y == 0:
        ng = 1
    else:
        ng = SQRT2
    if self.weighted:
        ng *= node_b.weight
    return node_a.g + ng