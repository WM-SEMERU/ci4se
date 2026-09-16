def list_projects_search(self, searchstring):
    log.debug('List all projects with: %s' % searchstring)
    return self.collection('projects/search/%s.json' % quote_plus(searchstring)
        )