def main(argv):
    if flags.FLAGS.version:
        print('GRR server {}'.format(config_server.VERSION['packageversion']))
        return
    if not flags.FLAGS.component:
        raise ValueError('Need to specify which component to start.')
    if flags.FLAGS.component.startswith('worker'):
        worker.main([argv])
    elif flags.FLAGS.component.startswith('frontend'):
        frontend.main([argv])
    elif flags.FLAGS.component.startswith('admin_ui'):
        admin_ui.main([argv])
    else:
        raise ValueError('No valid component specified. Got: %s.' % flags.
            FLAGS.component)