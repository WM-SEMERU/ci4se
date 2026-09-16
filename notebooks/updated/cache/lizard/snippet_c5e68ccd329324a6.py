def _oai_to_xml(marc_oai):
    record = MARCXMLRecord(marc_oai)
    record.oai_marc = False
    return record.to_XML()