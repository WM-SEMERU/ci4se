def list_vm_images_sub(access_token, subscription_id):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/providers/Microsoft.Compute/images',
        '?api-version=', COMP_API])
    return do_get_next(endpoint, access_token)