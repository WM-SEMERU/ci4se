def _add_message_file(arg_parser, help_text):
    arg_parser.add_argument('--msg-file', type=argparse.FileType('r'), help
        =help_text)