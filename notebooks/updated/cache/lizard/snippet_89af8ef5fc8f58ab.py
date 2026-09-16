def get_assessment_part_ids_by_banks(self, bank_ids):
    id_list = []
    for assessment_part in self.get_assessment_parts_by_banks(bank_ids):
        id_list.append(assessment_part.get_id())
    return IdList(id_list)