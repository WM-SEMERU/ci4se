def schedule_job(self, j):
    job_id = uuid.uuid4().hex
    j.job_id = job_id
    session = self.sessionmaker()
    orm_job = ORMJob(id=job_id, state=j.state, app=self.app, namespace=self
        .namespace, obj=j)
    session.add(orm_job)
    try:
        session.commit()
    except Exception as e:
        logging.error('Got an error running session.commit(): {}'.format(e))
    return job_id