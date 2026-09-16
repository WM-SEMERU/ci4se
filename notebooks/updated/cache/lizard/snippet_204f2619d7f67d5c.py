def _replace_image(image_url, image_tag, ebook_folder, image_name=None):
    try:
        assert isinstance(image_tag, bs4.element.Tag)
    except AssertionError:
        raise TypeError('image_tag cannot be of type ' + str(type(image_tag)))
    if image_name is None:
        image_name = str(uuid.uuid4())
    try:
        image_full_path = os.path.join(ebook_folder, 'images')
        assert os.path.exists(image_full_path)
        image_extension = save_image(image_url, image_full_path, image_name)
        image_tag['src'] = 'images' + '/' + image_name + '.' + image_extension
    except ImageErrorException:
        image_tag.decompose()
    except AssertionError:
        raise ValueError(
            "%s doesn't exist or doesn't contain a subdirectory images" %
            ebook_folder)
    except TypeError:
        image_tag.decompose()