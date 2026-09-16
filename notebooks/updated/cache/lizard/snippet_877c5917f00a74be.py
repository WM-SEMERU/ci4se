def question_image_filepath(instance, filename):
    return '/'.join(['images', str(instance.question_level), str(instance.
        question_level_id), binascii.b2a_hex(os.urandom(15)), filename])