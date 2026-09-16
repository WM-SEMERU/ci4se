def main(args):
    random.seed()
    temp_dir = tempfile.mkdtemp()
    logging.info('Created temporary directory: %s', temp_dir)
    validator = SubmissionValidator(source_dir=args.source_dir, target_dir=
        args.target_dir, temp_dir=temp_dir, do_copy=args.copy, use_gpu=args
        .use_gpu, containers_file=args.containers_file)
    validator.run()
    logging.info('Deleting temporary directory: %s', temp_dir)
    subprocess.call(['rm', '-rf', temp_dir])