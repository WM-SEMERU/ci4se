def from_time_struct(cls, time_struct):
    instance = super().__new__(cls, time_struct)
    instance.initialize(time_struct)
    return instance