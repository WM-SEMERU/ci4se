def increment_cell_value(self, column_family_id, column, int_value):
    column = _to_bytes(column)
    rule_pb = data_v2_pb2.ReadModifyWriteRule(family_name=column_family_id,
        column_qualifier=column, increment_amount=int_value)
    self._rule_pb_list.append(rule_pb)