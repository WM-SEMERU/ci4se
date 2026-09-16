def remove_file(config_map, file_key):
    if file_key[0] == '/':
        file_key = file_key[1:]
    client = boto3.client('s3', aws_access_key_id=config_map[
        'put_public_key'], aws_secret_access_key=config_map['put_private_key'])
    client.delete_object(Bucket=config_map['s3_bucket'], Key=file_key)