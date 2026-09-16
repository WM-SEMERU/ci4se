def run_container(self, image_id, service_name, **kwargs):
    run_kwargs = self.run_kwargs_for_service(service_name)
    run_kwargs.update(kwargs, relax=True)
    logger.debug('Running container in docker', image=image_id, params=
        run_kwargs)
    container_obj = self.client.containers.run(image=image_id, detach=True,
        **run_kwargs)
    log_iter = container_obj.logs(stdout=True, stderr=True, stream=True)
    mux = logmux.LogMultiplexer()
    mux.add_iterator(log_iter, plainLogger)
    return container_obj.id