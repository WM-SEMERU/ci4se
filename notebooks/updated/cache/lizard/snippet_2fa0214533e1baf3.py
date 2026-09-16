def main(args_list=None):
    print_version_info()
    if args_list is None:
        args_list = sys.argv[1:]
    args = arg_parser.parse_args(args_list)
    variants = variant_collection_from_args(args)
    effects = variants.effects()
    if args.only_coding:
        effects = effects.drop_silent_and_noncoding()
    if args.one_per_variant:
        variant_to_effect_dict = effects.top_priority_effect_per_variant()
        effects = effects.clone_with_new_elements(list(
            variant_to_effect_dict.values()))
    effects_dataframe = effects.to_dataframe()
    logger.info('\n%s', effects)
    if args.output_csv:
        effects_dataframe.to_csv(args.output_csv, index=False)