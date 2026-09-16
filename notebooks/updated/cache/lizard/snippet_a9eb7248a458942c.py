def append_transformation(self, transformation, return_alternatives=False,
    clear_redo=True):
    if clear_redo:
        self._undone = []
    if return_alternatives and transformation.is_one_to_many:
        ranked_list = transformation.apply_transformation(self.
            final_structure, return_ranked_list=return_alternatives)
        input_structure = self.final_structure.as_dict()
        alts = []
        for x in ranked_list[1:]:
            s = x.pop('structure')
            actual_transformation = x.pop('transformation', transformation)
            hdict = actual_transformation.as_dict()
            hdict['input_structure'] = input_structure
            hdict['output_parameters'] = x
            self.final_structure = s
            d = self.as_dict()
            d['history'].append(hdict)
            d['final_structure'] = s.as_dict()
            alts.append(TransformedStructure.from_dict(d))
        x = ranked_list[0]
        s = x.pop('structure')
        actual_transformation = x.pop('transformation', transformation)
        hdict = actual_transformation.as_dict()
        hdict['input_structure'] = self.final_structure.as_dict()
        hdict['output_parameters'] = x
        self.history.append(hdict)
        self.final_structure = s
        return alts
    else:
        s = transformation.apply_transformation(self.final_structure)
        hdict = transformation.as_dict()
        hdict['input_structure'] = self.final_structure.as_dict()
        hdict['output_parameters'] = {}
        self.history.append(hdict)
        self.final_structure = s