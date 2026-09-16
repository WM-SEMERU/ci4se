def init_queue():

    def action(queue):
        queue.declare()
        click.secho('Indexing queue has been initialized.', fg='green')
        return queue
    return action