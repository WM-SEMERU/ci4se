def validators(*chained_validators):

    def validator_chain(match):
        for chained_validator in chained_validators:
            if not chained_validator(match):
                return False
        return True
    return validator_chain