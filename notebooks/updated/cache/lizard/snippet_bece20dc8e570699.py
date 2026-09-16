def format_header_cell(val):
    return re.sub('_', ' ', re.sub('(_Px_)', '(', re.sub('(_xP_)', ')', str
        (val))))