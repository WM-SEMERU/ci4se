def _update(self, commit=False):
    votes = Vote.objects.filter(content_type=self.get_content_type(),
        object_id=self.instance.pk, key=self.field.key)
    obj_score = sum([v.score for v in votes])
    obj_votes = len(votes)
    score, created = Score.objects.get_or_create(content_type=self.
        get_content_type(), object_id=self.instance.pk, key=self.field.key,
        defaults=dict(score=obj_score, votes=obj_votes))
    if not created:
        score.score = obj_score
        score.votes = obj_votes
        score.save()
    self.score = obj_score
    self.votes = obj_votes
    if commit:
        self.instance.save()