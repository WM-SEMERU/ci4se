def is_supported(self, target):
    if target.lower() not in self.targets_mcu_list:
        logging.debug('Target not found in definitions')
        return False
    mcu_record = self.targets.get_mcu_record(target
        ) if self.mcus.get_mcu_record(target
        ) is None else self.mcus.get_mcu_record(target)
    if self.tool:
        try:
            for k, v in mcu_record['tool_specific'].items():
                if k == self.tool:
                    return True
        except (TypeError, KeyError) as err:
            pass
        return False
    else:
        return True