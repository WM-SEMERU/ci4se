def repeat(self):
    info = self._get_command_info(CommandInfo_pb2.ChangeRepeatMode)
    return None if info is None else info.repeatMode