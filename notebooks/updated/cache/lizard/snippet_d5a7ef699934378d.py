def find_images(ami_name=None, executable_by=None, owners=None, image_ids=
    None, tags=None, region=None, key=None, keyid=None, profile=None,
    return_objs=False):
    retries = 30
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    while retries:
        try:
            filter_parameters = {'filters': {}}
            if image_ids:
                filter_parameters['image_ids'] = [image_ids]
            if executable_by:
                filter_parameters['executable_by'] = [executable_by]
            if owners:
                filter_parameters['owners'] = [owners]
            if ami_name:
                filter_parameters['filters']['name'] = ami_name
            if tags:
                for tag_name, tag_value in six.iteritems(tags):
                    filter_parameters['filters']['tag:{0}'.format(tag_name)
                        ] = tag_value
            images = conn.get_all_images(**filter_parameters)
            log.debug('The filters criteria %s matched the following images:%s'
                , filter_parameters, images)
            if images:
                if return_objs:
                    return images
                return [image.id for image in images]
            else:
                return False
        except boto.exception.BotoServerError as exc:
            if exc.error_code == 'Throttling':
                log.debug('Throttled by AWS API, will retry in 5 seconds...')
                time.sleep(5)
                retries -= 1
                continue
            log.error('Failed to convert AMI name `%s` to an AMI ID: %s',
                ami_name, exc)
            return False
    return False