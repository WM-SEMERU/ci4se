def suggest_charges(self, tolerance=0.1):
    recommendations = {}
    for def_type in self.defect_types:
        test_charges = np.arange(np.min(self.stable_charges[def_type]) - 1,
            np.max(self.stable_charges[def_type]) + 2)
        test_charges = [charge for charge in test_charges if charge not in
            self.finished_charges[def_type]]
        if len(self.transition_level_map[def_type].keys()):
            min_tl = min(self.transition_level_map[def_type].keys())
            if min_tl < tolerance:
                max_charge = max(self.transition_level_map[def_type][min_tl])
                test_charges = [charge for charge in test_charges if charge <
                    max_charge]
            max_tl = max(self.transition_level_map[def_type].keys())
            if max_tl > self.band_gap - tolerance:
                min_charge = min(self.transition_level_map[def_type][max_tl])
                test_charges = [charge for charge in test_charges if charge >
                    min_charge]
        else:
            test_charges = [charge for charge in test_charges if charge not in
                self.stable_charges[def_type]]
        recommendations[def_type] = test_charges
    return recommendations