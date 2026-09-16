def main_hrun():
    parser = argparse.ArgumentParser(description=
        'Tools for http(s) test. Base on rtsf.')
    parser.add_argument('--log-level', default='INFO', help=
        'Specify logging level, default is INFO.')
    parser.add_argument('--log-file', help='Write logs to specified file path.'
        )
    parser.add_argument('case_file', help='yaml testcase file')
    color_print('httpdriver {}'.format(__version__), 'GREEN')
    args = parser.parse_args()
    logger.setup_logger(args.log_level, args.log_file)
    runner = TestRunner(runner=HttpDriver).run(args.case_file)
    html_report = runner.gen_html_report()
    color_print('report: {}'.format(html_report))