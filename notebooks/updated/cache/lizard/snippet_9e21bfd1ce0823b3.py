def _compare_operation(self, order, cell, include_smaller, operation):
    for order_i in range(0, order):
        shift = 2 * (order - order_i)
        cell_i = cell >> shift
        if cell_i in self._orders[order_i]:
            if operation == 'check':
                return True
            elif operation == 'remove':
                self._orders[order_i].remove(cell_i)
                self.add(order_i + 1, range(cell_i << 2, cell_i + 1 << 2))
            elif operation == 'inter':
                return [(order, (cell,))]
    if cell in self._orders[order]:
        if operation == 'check':
            return True
        elif operation == 'remove':
            self._orders[order].remove(cell)
        elif operation == 'inter':
            return [(order, (cell,))]
    result = []
    if include_smaller:
        for order_i in range(order + 1, MAX_ORDER + 1):
            shift = 2 * (order_i - order)
            cells = []
            for cell_i in self._orders[order_i]:
                if cell_i >> shift == cell:
                    if operation == 'check':
                        return True
                    elif operation == 'remove' or operation == 'inter':
                        cells.append(cell_i)
            if operation == 'remove':
                for cell_i in cells:
                    self._orders[order_i].remove(cell_i)
            elif operation == 'inter':
                if cells:
                    result.append((order_i, cells))
    if operation == 'check':
        return False
    elif operation == 'inter':
        return result