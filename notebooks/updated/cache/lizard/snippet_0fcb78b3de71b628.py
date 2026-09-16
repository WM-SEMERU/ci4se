def _derX(self, x, y):
    if _isscalar(x):
        x_pos = max(min(self.xSearchFunc(self.x_list, x), self.x_n - 1), 1)
        y_pos = max(min(self.ySearchFunc(self.y_list, y), self.y_n - 1), 1)
    else:
        x_pos = self.xSearchFunc(self.x_list, x)
        x_pos[x_pos < 1] = 1
        x_pos[x_pos > self.x_n - 1] = self.x_n - 1
        y_pos = self.ySearchFunc(self.y_list, y)
        y_pos[y_pos < 1] = 1
        y_pos[y_pos > self.y_n - 1] = self.y_n - 1
    beta = (y - self.y_list[y_pos - 1]) / (self.y_list[y_pos] - self.y_list
        [y_pos - 1])
    dfdx = ((1 - beta) * self.f_values[x_pos, y_pos - 1] + beta * self.
        f_values[x_pos, y_pos] - ((1 - beta) * self.f_values[x_pos - 1, 
        y_pos - 1] + beta * self.f_values[x_pos - 1, y_pos])) / (self.
        x_list[x_pos] - self.x_list[x_pos - 1])
    return dfdx