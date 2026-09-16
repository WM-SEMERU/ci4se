def deserialize(self, apic_frame):
    return Image(data=apic_frame.data, desc=apic_frame.desc, type=
        apic_frame.type)