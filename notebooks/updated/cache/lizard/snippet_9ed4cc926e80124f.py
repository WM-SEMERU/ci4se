def main(argv=None):
    try:
        _name_of_script, filepath = argv
    except ValueError:
        raise ValueError(argv)
    make_confidence_report(filepath=filepath, test_start=FLAGS.test_start,
        test_end=FLAGS.test_end, which_set=FLAGS.which_set, report_path=
        FLAGS.report_path, mc_batch_size=FLAGS.mc_batch_size, nb_iter=FLAGS
        .nb_iter, base_eps_iter=FLAGS.base_eps_iter, batch_size=FLAGS.
        batch_size, save_advx=FLAGS.save_advx)