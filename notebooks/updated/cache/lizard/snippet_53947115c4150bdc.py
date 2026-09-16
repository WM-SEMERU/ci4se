def discover_region(self, move_x, move_y):
    field_list = deque([(move_y, move_x)])
    while len(field_list) != 0:
        field = field_list.popleft()
        tl_idx, br_idx, region_sum = self.get_region(field[1], field[0])
        if region_sum == 0:
            self.info_map[field[0], field[1]] = region_sum
            region_mat = self.info_map[tl_idx[0]:br_idx[0] + 1, tl_idx[1]:
                br_idx[1] + 1]
            x_list, y_list = np.nonzero(region_mat == 11)
            for x_idx, y_idx in zip(x_list, y_list):
                field_temp = x_idx + max(field[0] - 1, 0), y_idx + max(
                    field[1] - 1, 0)
                if field_temp not in field_list:
                    field_list.append(field_temp)
        elif region_sum > 0:
            self.info_map[field[0], field[1]] = region_sum