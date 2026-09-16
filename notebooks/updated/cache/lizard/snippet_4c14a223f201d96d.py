def validate_api_compatibility(args):
    if args.api_version and args.api_version < MINIMUM_SUPPORTED_API_VERSION:
        print(
            'ERROR: Given API version: {0}. Minimum supported API version: {1}'
            .format(args.api_version, MINIMUM_SUPPORTED_API_VERSION))