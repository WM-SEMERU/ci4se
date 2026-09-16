def set_dir(self, dir_):
    self.__lock_set_dir(dir_)
    self.__lock_auto_load()
    self.__lock_update_table()
    self.__update_info()
    self.__update_window_title()