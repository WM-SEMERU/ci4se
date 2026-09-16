def delete_assessment_part(self, assessment_part_id):
    if not isinstance(assessment_part_id, ABCId):
        raise errors.InvalidArgument('the argument is not a valid OSID Id')
    collection = JSONClientValidated('assessment_authoring', collection=
        'AssessmentPart', runtime=self._runtime)
    if collection.find({'assessmentPartId': str(assessment_part_id)}).count(
        ) != 0:
        raise errors.IllegalState(
            'there are still AssessmentParts associated with this AssessmentPart'
            )
    collection = JSONClientValidated('assessment_authoring', collection=
        'AssessmentPart', runtime=self._runtime)
    try:
        apls = get_assessment_part_lookup_session(runtime=self._runtime,
            proxy=self._proxy)
        apls.use_unsequestered_assessment_part_view()
        apls.use_federated_bank_view()
        part = apls.get_assessment_part(assessment_part_id)
        part.delete()
    except AttributeError:
        collection.delete_one({'_id': ObjectId(assessment_part_id.
            get_identifier())})