def render_compressed(self, package, package_name, package_type):
    if settings.PIPELINE_ENABLED:
        return self.render_compressed_output(package, package_name,
            package_type)
    else:
        return self.render_compressed_sources(package, package_name,
            package_type)