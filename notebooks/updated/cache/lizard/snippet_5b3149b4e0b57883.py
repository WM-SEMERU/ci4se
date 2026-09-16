def load_file(self, file_path):
    self._log.info('Loading file: ' + file_path)
    agentml = etree.parse(file_path)
    self._schema.assertValid(agentml)
    root = etree.parse(file_path).getroot()
    defaults = {}

    def parse_element(element):
        for child in element:
            if child.tag == 'init':
                Init(self, child, file_path)
            if child.tag == 'group':
                self._log.info('Setting Trigger group: {group}'.format(
                    group=child.get('name')))
                defaults['groups'] = {child.get('name')}
                parse_element(child)
                del defaults['groups']
                continue
            if child.tag == 'topic':
                self._log.info('Setting Trigger topic: {topic}'.format(
                    topic=child.get('name')))
                defaults['topic'] = child.get('name')
                parse_element(child)
                del defaults['topic']
                continue
            if child.tag == 'emotion':
                self._log.info('Setting Trigger emotion: {emotion}'.format(
                    emotion=child.get('name')))
                defaults['emotion'] = child.get('name')
                parse_element(child)
                del defaults['emotion']
                continue
            if child.tag == 'trigger':
                try:
                    self.add_trigger(Trigger(self, child, file_path, **
                        defaults))
                except AgentMLError:
                    self._log.warn('Skipping Trigger due to an error',
                        exc_info=True)
    parse_element(root)