def save_archive(archive):
    _assert_obj_type(archive, obj_type=DBArchive)
    _get_handler().store_object(archive)
    return archive.to_comm(light_request=True)