def outlook(self, qs):
    csvf = writer(sys.stdout)
    columns = ['Name', 'E-mail Address', 'Notes', 'E-mail 2 Address',
        'E-mail 3 Address', 'Mobile Phone', 'Pager', 'Company', 'Job Title',
        'Home Phone', 'Home Phone 2', 'Home Fax', 'Home Address',
        'Business Phone', 'Business Phone 2', 'Business Fax',
        'Business Address', 'Other Phone', 'Other Fax', 'Other Address']
    csvf.writerow(columns)
    empty = [''] * (len(columns) - 2)
    for ent in qs:
        csvf.writerow([full_name(**ent), ent['email']] + empty)