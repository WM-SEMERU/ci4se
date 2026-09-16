async def container(self, container=None, container_type=None, params=None):
    if hasattr(container_type, 'serialize_archive'):
        container = container_type() if container is None else container
        return await container.serialize_archive(self, elem=container,
            elem_type=container_type, params=params)
    if self.writing:
        return await self._dump_container(self.iobj, container,
            container_type, params)
    else:
        return await self._load_container(self.iobj, container_type, params
            =params, container=container)