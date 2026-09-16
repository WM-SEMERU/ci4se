def register_hit_type(self, title, description, reward, duration_hours,
    keywords, qualifications):
    reward = str(reward)
    duration_secs = int(datetime.timedelta(hours=duration_hours).
        total_seconds())
    hit_type = self.mturk.create_hit_type(Title=title, Description=
        description, Reward=reward, AssignmentDurationInSeconds=
        duration_secs, Keywords=','.join(keywords),
        AutoApprovalDelayInSeconds=0, QualificationRequirements=qualifications)
    return hit_type['HITTypeId']