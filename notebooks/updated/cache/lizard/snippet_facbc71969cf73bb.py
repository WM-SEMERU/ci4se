def upload(clk_json, project, apikey, server, output, verbose):
    if verbose:
        log('Uploading CLK data from {}'.format(clk_json.name))
        log('To Entity Matching Server: {}'.format(server))
        log('Project ID: {}'.format(project))
        log('Uploading CLK data to the server')
    response = project_upload_clks(server, project, apikey, clk_json)
    if verbose:
        log(response)
    json.dump(response, output)