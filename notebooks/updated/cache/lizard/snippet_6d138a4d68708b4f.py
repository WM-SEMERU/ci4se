def _create_folder(self):
    import os
    from labpack.platforms.localhost import localhostClient
    from labpack.records.id import labID
    record_id = labID()
    collection_name = 'Watson Speech2Text'
    localhost_client = localhostClient()
    app_folder = localhost_client.app_data(org_name=__team__, prod_name=
        __module__)
    if localhost_client.os in ('Linux', 'FreeBSD', 'Solaris'):
        collection_name = collection_name.replace(' ', '-').lower()
    collection_folder = os.path.join(app_folder, collection_name)
    clip_folder = os.path.join(collection_folder, record_id.id24)
    if not os.path.exists(clip_folder):
        os.makedirs(clip_folder)
    return clip_folder