def get_upload_report(self):
    project = self.remote_store.fetch_remote_project(self.
        project_name_or_id, must_exist=True, include_children=False)
    report = UploadReport(project.name)
    report.walk_project(self.local_project)
    return report.get_content()