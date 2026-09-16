def parse_a_hall(self, hall):
    if hall not in self.hall_to_link:
        return None
    page = requests.get(self.hall_to_link[hall], timeout=60)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()
    washers = {'open': 0, 'running': 0, 'out_of_order': 0, 'offline': 0,
        'time_remaining': []}
    dryers = {'open': 0, 'running': 0, 'out_of_order': 0, 'offline': 0,
        'time_remaining': []}
    detailed = []
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            machine_type = cols[1].getText()
            if machine_type == 'Washer':
                washers = Laundry.update_machine_object(cols, washers)
            elif machine_type == 'Dryer':
                dryers = Laundry.update_machine_object(cols, dryers)
            if machine_type in ['Washer', 'Dryer']:
                try:
                    time = int(cols[3].getText().split(' ')[0])
                except ValueError:
                    time = 0
                detailed.append({'id': int(cols[0].getText().split(' ')[1][
                    1:]), 'type': cols[1].getText().lower(), 'status': cols
                    [2].getText(), 'time_remaining': time})
    machines = {'washers': washers, 'dryers': dryers, 'details': detailed}
    return machines