def store_field(self, state, field_name, field_type, value):
    field_ref = SimSootValue_InstanceFieldRef(self.heap_alloc_id, self.type,
        field_name, field_type)
    state.memory.store(field_ref, value)