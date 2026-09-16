async def _check_latch_data(self, key, data):
    process = False
    latching_entry = self.latch_map.get(key)
    if latching_entry[Constants.LATCH_STATE] == Constants.LATCH_ARMED:
        if latching_entry[Constants.LATCHED_THRESHOLD_TYPE
            ] == Constants.LATCH_EQ:
            if data == latching_entry[Constants.LATCH_DATA_TARGET]:
                process = True
        elif latching_entry[Constants.LATCHED_THRESHOLD_TYPE
            ] == Constants.LATCH_GT:
            if data > latching_entry[Constants.LATCH_DATA_TARGET]:
                process = True
        elif latching_entry[Constants.LATCHED_THRESHOLD_TYPE
            ] == Constants.LATCH_GTE:
            if data >= latching_entry[Constants.LATCH_DATA_TARGET]:
                process = True
        elif latching_entry[Constants.LATCHED_THRESHOLD_TYPE
            ] == Constants.LATCH_LT:
            if data < latching_entry[Constants.LATCH_DATA_TARGET]:
                process = True
        elif latching_entry[Constants.LATCHED_THRESHOLD_TYPE
            ] == Constants.LATCH_LTE:
            if data <= latching_entry[Constants.LATCH_DATA_TARGET]:
                process = True
        if process:
            latching_entry[Constants.LATCHED_DATA] = data
            await self._process_latching(key, latching_entry)