def create_or_update(cls, course_video, file_name=None, image_data=None,
    generated_images=None):
    video_image, created = cls.objects.get_or_create(course_video=course_video)
    if image_data:
        if not created and VideoImage.objects.filter(image=video_image.image
            ).count() == 1:
            video_image.image.delete()
        with closing(image_data) as image_file:
            file_name = '{uuid}{ext}'.format(uuid=uuid4().hex, ext=os.path.
                splitext(file_name)[1])
            try:
                video_image.image.save(file_name, image_file)
            except Exception:
                logger.exception(
                    'VAL: Video Image save failed to storage for course_id [%s] and video_id [%s]'
                    , course_video.course_id, course_video.video.edx_video_id)
                raise
    else:
        if generated_images:
            video_image.generated_images = generated_images
            if not video_image.image.name:
                file_name = generated_images[0]
        video_image.image.name = file_name
    video_image.save()
    return video_image, created