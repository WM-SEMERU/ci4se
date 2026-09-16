def determine_module_class(path, class_path):
    if not class_path:
        basename = os.path.basename(path)
        if basename.endswith('.sls'):
            class_path = 'runway.module.serverless.Serverless'
        elif basename.endswith('.tf'):
            class_path = 'runway.module.terraform.Terraform'
        elif basename.endswith('.cdk'):
            class_path = 'runway.module.cdk.CloudDevelopmentKit'
        elif basename.endswith('.cfn'):
            class_path = 'runway.module.cloudformation.CloudFormation'
    if not class_path:
        if os.path.isfile(os.path.join(path, 'serverless.yml')):
            class_path = 'runway.module.serverless.Serverless'
        elif glob.glob(os.path.join(path, '*.tf')):
            class_path = 'runway.module.terraform.Terraform'
        elif os.path.isfile(os.path.join(path, 'cdk.json')) and os.path.isfile(
            os.path.join(path, 'package.json')):
            class_path = 'runway.module.cdk.CloudDevelopmentKit'
        elif glob.glob(os.path.join(path, '*.env')) or glob.glob(os.path.
            join(path, '*.yaml')) or glob.glob(os.path.join(path, '*.yml')):
            class_path = 'runway.module.cloudformation.CloudFormation'
    if not class_path:
        LOGGER.error('No module class found for %s', os.path.basename(path))
        sys.exit(1)
    return load_object_from_string(class_path)