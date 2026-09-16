def generate_localized_events(generator):
    if 'i18n_subsites' in generator.settings['PLUGINS']:
        if not os.path.exists(generator.settings['OUTPUT_PATH']):
            os.makedirs(generator.settings['OUTPUT_PATH'])
        for e in events:
            if 'lang' in e.metadata:
                localized_events[e.metadata['lang']].append(e)
            else:
                log.debug('event %s contains no lang attribute' % (e.
                    metadata['title'],))