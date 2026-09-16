def show_profiles_from_aws_credentials_file(credentials_files=[
    aws_credentials_file, aws_config_file]):
    profiles = get_profiles_from_aws_credentials_file(credentials_files)
    for profile in set(profiles):
        printInfo(' * %s' % profile)