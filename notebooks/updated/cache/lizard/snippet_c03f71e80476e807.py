def remove_contributor(self, project_id, email, language):
    self._run(url_path='contributors/remove', id=project_id, email=email,
        language=language)
    return True