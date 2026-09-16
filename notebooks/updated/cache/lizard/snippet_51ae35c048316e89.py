def clear_all(self):
    logger.info('Clearing ALL Labels and LabelKeys.')
    self.session.query(Label).delete(synchronize_session='fetch')
    self.session.query(LabelKey).delete(synchronize_session='fetch')