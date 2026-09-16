def _get_data_format_2and4(raw):
    try:
        base16_split = [raw[i:i + 2] for i in range(0, len(raw), 2)]
        selected_hexs = filter(lambda x: int(x, 16) < 128, base16_split)
        characters = [chr(int(c, 16)) for c in selected_hexs]
        data = ''.join(characters)
        index = data.find('ruu.vi/#')
        if index > -1:
            return data[index + 8:]
        else:
            index = data.find('r/')
            if index > -1:
                return data[index + 2:]
            return None
    except:
        return None