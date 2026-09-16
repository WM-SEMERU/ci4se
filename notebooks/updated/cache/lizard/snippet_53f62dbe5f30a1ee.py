def clone_fluent_contentitems_m2m_relationships(self, dst_obj):
    if not hasattr(self, 'contentitem_set'):
        return
    reliable_ordering = ['placeholder__slot', 'sort_order']
    for src_ci, dst_ci in zip(self.contentitem_set.order_by(*
        reliable_ordering), dst_obj.contentitem_set.order_by(*
        reliable_ordering)):
        for field, __ in src_ci._meta.get_m2m_with_model():
            field_name = field.name
            src_m2m = getattr(src_ci, field_name)
            dst_m2m = getattr(dst_ci, field_name)
            dst_m2m.add(*src_m2m.all())