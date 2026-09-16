def _get_asconv_headers(mosaic):
    asconv_headers = re.findall('### ASCCONV BEGIN(.*)### ASCCONV END ###',
        mosaic[Tag(41, 4128)].value.decode(encoding='ISO-8859-1'), re.DOTALL)[0
        ]
    return asconv_headers