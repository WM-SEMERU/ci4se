def _init_map(self):
    DecimalValuesFormRecord._init_map(self)
    IntegerValuesFormRecord._init_map(self)
    TextAnswerFormRecord._init_map(self)
    FilesAnswerFormRecord._init_map(self)
    FeedbackAnswerFormRecord._init_map(self)
    super(CalculationInteractionFeedbackAndFilesAnswerFormRecord, self
        )._init_map()
    self.my_osid_object_form._my_map['toleranceMode'
        ] = self._tolerance_mode_metadata['default_string_values'][0]