def validate_product_equation(poi=None):
    from . import utils
    from . import validators
    container_dir, product_name = tasks.get_poi_tuple(poi=poi)
    feature_list = utils.get_features_from_equation(container_dir, product_name
        )
    ordering_constraints = utils.get_feature_order_constraints(container_dir)
    spec_path = utils.get_feature_ide_paths(container_dir, product_name
        ).product_spec_path
    print('*** Starting product.equation validation')
    print('\tChecking feature order')
    feature_order_validator = validators.FeatureOrderValidator(feature_list,
        ordering_constraints)
    feature_order_validator.check_order()
    if feature_order_validator.has_errors():
        print('\t\txxx ERROR in your product.equation feature order xxx')
        for error in feature_order_validator.get_violations():
            print('\t\t\t', error[1])
    else:
        print('\t\tOK')
    print('\tChecking functional product spec')
    if not os.path.exists(spec_path):
        print(
            """		Skipped - No product spec exists.
		You may create a product spec if you want to ensure that
		required functional features are represented in the product equation
		=> Create spec file featuremodel/productline/<container>/product_spec.json"""
            )
        return
    spec_validator = validators.ProductSpecValidator(spec_path,
        product_name, feature_list)
    if not spec_validator.is_valid():
        if spec_validator.get_errors_mandatory():
            print('\t\tERROR: The following feature are missing',
                spec_validator.get_errors_mandatory())
        if spec_validator.get_errors_never():
            print('\t\tERROR: The following feature are not allowed',
                spec_validator.get_errors_never())
    else:
        print('\t\tOK')
    if feature_order_validator.has_errors() or spec_validator.has_errors():
        sys.exit(1)