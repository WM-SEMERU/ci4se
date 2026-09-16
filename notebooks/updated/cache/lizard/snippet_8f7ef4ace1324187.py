def write_generator_data(self, file):
    for generator in self.case.generators:
        vals = []
        vals.append(generator.bus._i)
        vals.append('1 ')
        vals.append(generator.p)
        vals.append(generator.q)
        vals.append(generator.q_max)
        vals.append(generator.q_min)
        vals.append(generator.v_magnitude)
        vals.append(0)
        vals.append(generator.base_mva)
        vals.extend([0.0, 1.0, 0.0, 0.0, 0.0])
        vals.append(generator.online)
        vals.append(100.0)
        vals.append(generator.p_max)
        vals.append(generator.p_min)
        vals.extend([1, 1.0])
        file.write(
            """%6d,'%s',%10.3f,%10.3f,%10.3f,%10.3f,%10.5f,%6d,%10.3f,%10.5f,%10.5f,%10.5f,%10.5f,%7.5f,%d,%7.1f,%10.3f,%10.3f,%4d,%6.4f
"""
             % tuple(vals))
    file.write(
        ' 0 / END OF GENERATOR DATA, BEGIN NON-TRANSFORMER BRANCH DATA\n')