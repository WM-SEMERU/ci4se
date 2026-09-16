def index():
    mapping = cfg['UNAPI_FORMAT_MAPPING']
    names = {mapping[k]: k for k in mapping}
    identifier = request.values.get('id', type=int)
    format_ = request.values.get('format')
    format_ = mapping.get(format_, format_)
    if identifier and format_:
        return redirect(url_for('record.metadata', recid=identifier, of=
            format_))
    formats = [{'name': names[of], 'type': values['content_type'], 'docs':
        values.get('url')} for of, values in iteritems(output_formats) if 
        of in names]
    response = make_response(render_template('unapi/index.xml', identifier=
        identifier, formats=formats))
    response.headers['Content-Type'] = 'application/xml'
    return response