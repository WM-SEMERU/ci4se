def save_unstructured_document(self, ehr_username, patient_id, encounter_id,
    document_content):
    doc_xml = ("<docParams><item name='documentCommand' value='I'/>" +
        "<item name='documentType'  value='Chart'/>" +
        "<item name='authorCode' value='ResLet'/>" +
        "<item name='ahsEncounterID' value='@@ENCOUNTERID@@'/>" +
        "<item name='OrganizationID' value=''/>" +
        "<item name='accessionValue' value=''/>" +
        "<item name='appGroup' value='TouchWorks'/></docParams>")
    doc_xml = doc_xml.replace('@@ENCOUNTERID@@', str(encounter_id))
    print(doc_xml)
    magic = self._magic_json(action=TouchWorksMagicConstants.
        ACTION_SAVE_UNSTRUCTURED_DATA, patient_id=patient_id, user_id=
        ehr_username, parameter1=doc_xml, parameter2=document_content)
    response = self._http_request(TouchWorksEndPoints.MAGIC_JSON, data=magic)
    result = self._get_results_or_raise_if_magic_invalid(magic, response,
        TouchWorksMagicConstants.RESULT_SAVE_UNSTRUCTURED_DATA)
    return result