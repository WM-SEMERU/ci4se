def linkedin(self, qs):
    csvf = writer(sys.stdout)
    csvf.writerow(['First Name', 'Last Name', 'Email'])
    for ent in qs:
        csvf.writerow([ent['first_name'], ent['last_name'], ent['email']])