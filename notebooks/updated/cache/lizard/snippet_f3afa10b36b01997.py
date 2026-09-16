def _init_map(self, record_types=None, **kwargs):
    osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
    self._my_map['outputScore'] = self._output_score_default
    self._my_map['gradeSystemId'] = str(kwargs['grade_system_id'])
    self._my_map['inputScoreEndRange'] = self._input_score_end_range_default
    self._my_map['inputScoreStartRange'
        ] = self._input_score_start_range_default
    self._my_map['assignedGradebookIds'] = [str(kwargs['gradebook_id'])]