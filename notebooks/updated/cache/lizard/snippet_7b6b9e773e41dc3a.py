def error_messages(self, driver_id=None):
    if driver_id is not None:
        assert isinstance(driver_id, ray.DriverID)
        return self._error_messages(driver_id)
    error_table_keys = self.redis_client.keys(ray.gcs_utils.
        TablePrefix_ERROR_INFO_string + '*')
    driver_ids = [key[len(ray.gcs_utils.TablePrefix_ERROR_INFO_string):] for
        key in error_table_keys]
    return {binary_to_hex(driver_id): self._error_messages(ray.DriverID(
        driver_id)) for driver_id in driver_ids}