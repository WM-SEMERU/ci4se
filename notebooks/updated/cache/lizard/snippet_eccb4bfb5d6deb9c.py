def run_solr_on(solrInstance, category, id, fields):
    query = (solrInstance.value + 'select?q=*:*&fq=document_category:"' +
        category.value + '"&fq=id:"' + id + '"&fl=' + fields +
        '&wt=json&indent=on')
    response = requests.get(query)
    return response.json()['response']['docs'][0]