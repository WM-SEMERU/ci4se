def delocalization_analysis(self, defect_entry):
    defect_entry.parameters.update({'is_compatible': True})
    if 'freysoldt_meta' in defect_entry.parameters.keys():
        defect_entry = self.is_freysoldt_delocalized(defect_entry)
    else:
        print(
            """Insufficient information provided for performing Freysoldt correction delocalization analysis.
Cannot perform planar averaged electrostatic potential compatibility analysis."""
            )
    if 'kumagai_meta' in defect_entry.parameters.keys():
        defect_entry = self.is_kumagai_delocalized(defect_entry)
    else:
        print(
            """Insufficient information provided for performing Kumagai correction delocalization analysis.
Cannot perform atomic site averaged electrostatic potential compatibility analysis."""
            )
    if 'final_defect_structure' in defect_entry.parameters.keys(
        ) and 'initial_defect_structure' in defect_entry.parameters.keys(
        ) and 'sampling_radius' in defect_entry.parameters.keys():
        defect_entry = self.is_final_relaxed_structure_delocalized(defect_entry
            )
    else:
        print(
            'Insufficient information provided in defect_entry.parameters. Cannot perform full structure site relaxation compatibility analysis.'
            )
    return defect_entry