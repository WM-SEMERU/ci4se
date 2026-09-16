def delete_dagobah(self, dagobah_id):
    rec = self.dagobah_coll.find_one({'_id': dagobah_id})
    for job in rec.get('jobs', []):
        if 'job_id' in job:
            self.delete_job(job['job_id'])
    self.log_coll.remove({'parent_id': dagobah_id})
    self.dagobah_coll.remove({'_id': dagobah_id})