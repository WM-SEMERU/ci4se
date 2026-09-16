def launch_job(job_spec):
    project_id = 'projects/{}'.format(text_encoder.native_to_unicode(
        default_project()))
    credentials = GoogleCredentials.get_application_default()
    cloudml = discovery.build('ml', 'v1', credentials=credentials,
        cache_discovery=False)
    request = cloudml.projects().jobs().create(body=job_spec, parent=project_id
        )
    request.execute()