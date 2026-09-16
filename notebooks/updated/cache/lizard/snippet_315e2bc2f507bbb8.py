def topic_path(cls, project, topic):
    return google.api_core.path_template.expand(
        'projects/{project}/topics/{topic}', project=project, topic=topic)