def delete(self):

    def set_rw(operation, name, exc):
        os.chmod(name, stat.S_IWRITE)
    directory = self.project.node_working_directory(self)
    if os.path.exists(directory):
        try:
            yield from wait_run_in_executor(shutil.rmtree, directory,
                onerror=set_rw)
        except OSError as e:
            raise aiohttp.web.HTTPInternalServerError(text=
                'Could not delete the node working directory: {}'.format(e))