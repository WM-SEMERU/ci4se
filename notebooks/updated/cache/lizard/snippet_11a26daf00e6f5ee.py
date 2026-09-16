def transform_to_mods_multimono(marc_xml, uuid, url):
    marc_xml = _read_content_or_path(marc_xml)
    transformed = xslt_transformation(marc_xml, _absolute_template_path(
        'MARC21toMultiMonographTitle.xsl'))
    return _apply_postprocessing(marc_xml=marc_xml, xml=transformed, func=
        mods_postprocessor.postprocess_multi_mono, uuid=uuid, url=url)