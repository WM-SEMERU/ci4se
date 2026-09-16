def run(cli_args):
    from .core import Core
    c = Core(source_file=cli_args['--data-file'], schema_files=cli_args[
        '--schema-file'], extensions=cli_args['--extension'],
        strict_rule_validation=cli_args['--strict-rule-validation'],
        fix_ruby_style_regex=cli_args['--fix-ruby-style-regex'],
        allow_assertions=cli_args['--allow-assertions'], file_encoding=
        cli_args['--encoding'])
    c.validate()
    return c