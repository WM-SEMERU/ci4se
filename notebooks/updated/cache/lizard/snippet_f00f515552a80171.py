def get_container_id(self, container_id=None):
    if container_id == None and self.container_id == None:
        bot.exit('You must provide a container_id.')
    container_id = container_id or self.container_id
    return container_id