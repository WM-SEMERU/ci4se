def delete_cached_files(self, prefixes=[], suffixes=[]):
    for filename in listdir(self.cache_directory_path):
        delete = any([filename.endswith(ext) for ext in suffixes]) or any([
            filename.startswith(pre) for pre in prefixes])
        if delete:
            path = join(self.cache_directory_path, filename)
            logger.info('Deleting %s', path)
            remove(path)