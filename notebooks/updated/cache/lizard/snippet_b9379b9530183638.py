def on_created(self, event):
    if os.path.isdir(event.src_path):
        return
    logger.debug('File created: %s', event.src_path)
    name = self.file_name(event)
    try:
        result = self.target_class.from_config(name, yaml.load(open(event.
            src_path)))
    except Exception as e:
        logger.exception('Error when loading new config file %s: %s', event
            .src_path, str(e))
        return
    if not result:
        return
    self.on_add(self.target_class, name, result)