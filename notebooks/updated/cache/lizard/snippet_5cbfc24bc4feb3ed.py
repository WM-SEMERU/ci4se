def dump_to_pyc(co, python_version, output_dir):
    pyc_basename = ntpath.basename(co.co_filename)
    pyc_name = pyc_basename + '.pyc'
    if pyc_name not in IGNORE:
        logging.info('Extracting %s', pyc_name)
        pyc_header = _generate_pyc_header(python_version, len(co.co_code))
        destination = os.path.join(output_dir, pyc_name)
        pyc = open(destination, 'wb')
        pyc.write(pyc_header)
        marshaled_code = marshal.dumps(co)
        pyc.write(marshaled_code)
        pyc.close()
    else:
        logging.info('Skipping %s', pyc_name)