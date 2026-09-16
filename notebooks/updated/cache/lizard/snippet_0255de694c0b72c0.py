def increment_lessons(self, measure_vals, reward_buff_sizes=None):
    ret = {}
    if reward_buff_sizes:
        for brain_name, buff_size in reward_buff_sizes.items():
            if self._lesson_ready_to_increment(brain_name, buff_size):
                measure_val = measure_vals[brain_name]
                ret[brain_name] = self.brains_to_curriculums[brain_name
                    ].increment_lesson(measure_val)
    else:
        for brain_name, measure_val in measure_vals.items():
            ret[brain_name] = self.brains_to_curriculums[brain_name
                ].increment_lesson(measure_val)
    return ret