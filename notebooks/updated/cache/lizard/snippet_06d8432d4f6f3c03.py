def _property_table():
    url = (
        'http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,resolution,experimentalTechnique,releaseDate&service=wsfile&format=csv'
        )
    r = requests.get(url)
    p = pd.read_csv(StringIO(r.text)).set_index('structureId')
    return p