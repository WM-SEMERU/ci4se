def remove_video_for_course(course_id, edx_video_id):
    course_video = CourseVideo.objects.get(course_id=course_id,
        video__edx_video_id=edx_video_id)
    course_video.is_hidden = True
    course_video.save()