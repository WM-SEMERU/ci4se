def process_usufy(self, data):
    mode = 'usufy'
    info = []
    try:
        verifier = self.modes.get(mode, {}).get('extra_fields', {})
        for field in verifier.keys():
            regexp = verifier[field]
            values = re.findall(regexp, data)
            for val in values:
                aux = {}
                aux['type'] = field
                aux['value'] = val
                aux['attributes'] = []
                if aux not in info:
                    info.append(aux)
    except AttributeError as e:
        for field in self.fieldsRegExp[mode].keys():
            try:
                regexp = self.fieldsRegExp[mode][field]['start'
                    ] + '([^\\)]+)' + self.fieldsRegExp[mode][field]['end']
                tmp = re.findall(regexp, data)
                values = []
                for t in tmp:
                    if self.fieldsRegExp[mode][field]['end'] in t:
                        values.append(t.split(self.fieldsRegExp[mode][field
                            ]['end'])[0])
                    else:
                        values.append(t)
            except:
                regexp = self.fieldsRegExp[mode][field]
                values = re.findall(regexp, data)
            for val in values:
                aux = {}
                aux['type'] = field
                aux['value'] = val
                aux['attributes'] = []
                if aux not in info:
                    info.append(aux)
    return info