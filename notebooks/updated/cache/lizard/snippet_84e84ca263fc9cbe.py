def load_template_source(self, template_name, template_dirs=None):
    log.error('Calling zip loader')
    for folder in app_template_dirs:
        if '.zip/' in folder.replace('\\', '/'):
            lib_file, relative_folder = get_zip_file_and_relative_path(folder)
            log.error(lib_file, relative_folder)
            try:
                z = zipfile.ZipFile(lib_file)
                log.error(relative_folder + template_name)
                template_path_in_zip = os.path.join(relative_folder,
                    template_name).replace('\\', '/')
                source = z.read(template_path_in_zip)
            except (IOError, KeyError) as e:
                import traceback
                log.error(traceback.format_exc())
                try:
                    z.close()
                except:
                    pass
                continue
            z.close()
            template_path = '%s:%s' % (lib_file, template_path_in_zip)
            return source, template_path
    raise TemplateDoesNotExist(template_name)