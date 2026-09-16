def finish_assessment(self, assessment_taken_id):
    assessment_taken = self._get_assessment_taken(assessment_taken_id)
    assessment_taken_map = assessment_taken._my_map
    if assessment_taken.has_started() and not assessment_taken.has_ended():
        assessment_taken_map['completionTime'] = DateTime.utcnow()
        assessment_taken_map['ended'] = True
        collection = JSONClientValidated('assessment', collection=
            'AssessmentTaken', runtime=self._runtime)
        collection.save(assessment_taken_map)
    else:
        raise errors.IllegalState()