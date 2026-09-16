def _add_standard_attributes(cls):
    setattr(cls.context.new_class, cls.context.new_meta[
        'state_attribute_name'], cls.context.state_value)
    setattr(cls.context.new_class, cls.context.state_name, utils.state_property
        )
    setattr(cls.context.new_class, 'is_', utils.is_)
    setattr(cls.context.new_class, 'can_be_', utils.can_be_)
    setattr(cls.context.new_class, 'set_', utils.set_)