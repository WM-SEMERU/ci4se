def import_image(image_path, os_version):
    image_name = os.path.basename(image_path)
    print('\nChecking if image %s exists ...' % image_name)
    image_query_info = client.send_request('image_query', imagename=image_name)
    if image_query_info['overallRC']:
        print('Importing image %s ...' % image_name)
        url = 'file://' + image_path
        image_import_info = client.send_request('image_import', image_name,
            url, {'os_version': os_version})
        if image_import_info['overallRC']:
            raise RuntimeError('Failed to import image %s!\n%s' % (
                image_name, image_import_info))
        else:
            print('Succeeded to import image %s!' % image_name)
    else:
        print('Image %s already exists!' % image_name)