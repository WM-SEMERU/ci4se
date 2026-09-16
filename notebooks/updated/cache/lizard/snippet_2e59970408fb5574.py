def get_section_metrics(cls):
    return {'overview': {'activity_metrics': [Commits], 'author_metrics': [
        Authors], 'bmi_metrics': [], 'time_to_close_metrics': [],
        'projects_metrics': [Projects]}, 'com_channels': {
        'activity_metrics': [], 'author_metrics': []}, 'project_activity':
        {'metrics': [Commits, Authors]}, 'project_community': {
        'author_metrics': [Authors], 'people_top_metrics': [Authors],
        'orgs_top_metrics': [Organizations]}, 'project_process': {
        'bmi_metrics': [], 'time_to_close_metrics': [],
        'time_to_close_title': '', 'time_to_close_review_metrics': [],
        'time_to_close_review_title': '', 'patchsets_metrics': []}}