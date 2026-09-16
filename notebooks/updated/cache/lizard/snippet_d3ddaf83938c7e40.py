def get_patient(self, ehr_username, patient_id):
    magic = self._magic_json(action=TouchWorksMagicConstants.
        ACTION_GET_PATIENT_INFO, app_name=self._app_name, user_id=
        ehr_username, token=self._token.token, patient_id=patient_id)
    response = self._http_request(TouchWorksEndPoints.MAGIC_JSON, data=magic)
    result = self._get_results_or_raise_if_magic_invalid(magic, response,
        TouchWorksMagicConstants.RESULT_GET_PATIENT_INFO)
    return result