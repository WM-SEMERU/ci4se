def combining_search(self):
    start = self.get_pair(), (self.cube['L'], self.cube['U'], self.cube['F'
        ], self.cube['D'], self.cube['R'], self.cube['B'])
    return sum(path_actions(a_star_search(start, self.combining_successors,
        lambda x: len(x), self.combining_goal)), Formula())