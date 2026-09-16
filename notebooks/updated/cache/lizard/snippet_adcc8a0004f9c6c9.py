def from_message(cls, message):
    type_ = message.get_text()
    return cls(type_=type_, blob=message.asbytes())