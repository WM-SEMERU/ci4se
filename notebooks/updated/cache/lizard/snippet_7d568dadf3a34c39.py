def get_soql_fields(soql):
    soql_fields = re.search('(?<=select)(?s)(.*)(?=from)', soql, re.IGNORECASE)
    soql_fields = re.sub(' ', '', soql_fields.group())
    soql_fields = re.sub('\t', '', soql_fields)
    fields = re.split(',|\n|\r|', soql_fields)
    fields = [field for field in fields if field != '']
    return fields