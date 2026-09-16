def _create_messages(self, names, data, isDms=False):
    chats = {}
    empty_dms = []
    formatter = SlackFormatter(self.__USER_DATA, data)
    for name in names:
        dir_path = os.path.join(self._PATH, name)
        messages = []
        day_files = glob.glob(os.path.join(dir_path, '*.json'))
        if not day_files:
            if isDms:
                empty_dms.append(name)
            continue
        for day in sorted(day_files):
            with io.open(os.path.join(self._PATH, day), encoding='utf8') as f:
                day_messages = json.load(f)
                messages.extend([Message(formatter, d) for d in day_messages])
        chats[name] = messages
    if isDms:
        self._EMPTY_DMS = empty_dms
    return chats