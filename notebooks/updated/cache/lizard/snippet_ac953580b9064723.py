def safe_log_info(self, *info: str):
    self.__do_safe(lambda : self.logger.info(*info))