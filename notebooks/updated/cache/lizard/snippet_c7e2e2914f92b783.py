def _cache_update_needed(self, courseid):
    if courseid not in self._cache:
        return True
    try:
        descriptor_name = self._get_course_descriptor_path(courseid)
        last_update = {descriptor_name: self._filesystem.
            get_last_modification_time(descriptor_name)}
        translations_fs = self._filesystem.from_subfolder('$i18n')
        if translations_fs.exists():
            for f in translations_fs.list(folders=False, files=True,
                recursive=False):
                lang = f[0:len(f) - 3]
                if translations_fs.exists(lang + '.mo'):
                    last_update['$i18n/' + lang + '.mo'
                        ] = translations_fs.get_last_modification_time(lang +
                        '.mo')
    except:
        raise CourseNotFoundException()
    last_modif = self._cache[courseid][1]
    for filename, mftime in last_update.items():
        if filename not in last_modif or last_modif[filename] < mftime:
            return True
    return False