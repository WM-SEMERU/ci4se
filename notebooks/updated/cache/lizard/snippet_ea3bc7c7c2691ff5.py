def get_description(self, description_type='Abstract'):
    if 'descriptions' in self.xml:
        if isinstance(self.xml['descriptions']['description'], list):
            for description in self.xml['descriptions']['description']:
                if description_type in description:
                    return description[description_type]
        elif isinstance(self.xml['descriptions']['description'], dict):
            description = self.xml['descriptions']['description']
            if description_type in description:
                return description[description_type]
            elif len(description) == 1:
                return description.values()[0]
    return None