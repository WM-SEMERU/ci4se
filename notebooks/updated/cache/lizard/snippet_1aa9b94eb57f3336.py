def _variants(self, case_id, gemini_query):
    individuals = []
    case_obj = self.case(case_id)
    for individual in case_obj.individuals:
        individuals.append(individual)
    self.db = case_obj.variant_source
    self.variant_type = case_obj.variant_type
    gq = GeminiQuery(self.db)
    gq.run(gemini_query)
    index = 0
    for gemini_variant in gq:
        variant = None
        is_variant = self._is_variant(gemini_variant, individuals)
        if self.variant_type == 'snv' and not is_variant:
            variant = None
        else:
            index += 1
            logger.debug('Updating index to: {0}'.format(index))
            variant = self._format_variant(case_id=case_id, gemini_variant=
                gemini_variant, individual_objs=individuals, index=index)
        if variant:
            yield variant