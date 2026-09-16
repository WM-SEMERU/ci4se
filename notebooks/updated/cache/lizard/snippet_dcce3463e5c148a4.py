def vb_destroy_machine(name=None, timeout=10000):
    vbox = vb_get_box()
    log.info('Destroying machine %s', name)
    machine = vbox.findMachine(name)
    files = machine.unregister(2)
    progress = machine.deleteConfig(files)
    progress.waitForCompletion(timeout)
    log.info('Finished destroying machine %s', name)