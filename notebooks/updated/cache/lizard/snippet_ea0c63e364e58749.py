def get_assessment_ids_by_banks(self, bank_ids):
    id_list = []
    for assessment in self.get_assessments_by_banks(bank_ids):
        id_list.append(assessment.get_id())
    return IdList(id_list)