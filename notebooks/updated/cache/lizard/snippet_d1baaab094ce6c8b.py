def GetFormatSpecification(self):
    format_specification = specification.FormatSpecification(self.
        type_indicator)
    format_specification.AddNewSignature(b'1AY&SY', offset=4)
    return format_specification