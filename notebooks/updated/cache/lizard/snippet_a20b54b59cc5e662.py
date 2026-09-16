def create_for_object_attributes(item_type, faulty_attribute_name: str, hint):
    return TypeInformationRequiredError(
        "Cannot create instances of type {t}: constructor attribute '{a}' has an invalid PEP484 type hint: {h}."
        .format(t=str(item_type), a=faulty_attribute_name, h=hint))