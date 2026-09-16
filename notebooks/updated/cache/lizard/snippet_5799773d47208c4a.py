def process_links(self, links):
    links_list = []
    for link in links:
        if os.path.splitext(link)[1][1:].strip().lower() in self.format_list:
            links_list.append(link)
    return links_list