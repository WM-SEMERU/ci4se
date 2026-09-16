def start(self, discord_token, discord_client_id):
    self.button_toggle_text.set('Stop Modis')
    self.state = 'on'
    self.status_bar.set_status(1)
    logger.info('----------------STARTING DISCORD MODIS----------------')
    self.module_frame.clear_modules()
    from modis.discord_modis import main
    logger.debug('Creating event loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    self.discord_thread = threading.Thread(target=main.start, args=[
        discord_token, discord_client_id, loop, self.on_ready])
    logger.debug('Starting event loop')
    self.discord_thread.start()
    database_dir = '{}/modules'.format(os.path.dirname(os.path.realpath(
        __file__)))
    for module_name in os.listdir(database_dir):
        module_dir = '{}/{}'.format(database_dir, module_name)
        if os.path.isdir(module_dir) and not module_name.startswith('_'):
            module_event_handlers = os.listdir(module_dir)
            if '_ui.py' in module_event_handlers:
                import_name = '.discord_modis.modules.{}.{}'.format(module_name
                    , '_ui')
                logger.debug('Found module UI file {}'.format(import_name[23:])
                    )
                self.module_frame.add_module(module_name, importlib.
                    import_module(import_name, 'modis'))
            else:
                self.module_frame.add_module(module_name, None)