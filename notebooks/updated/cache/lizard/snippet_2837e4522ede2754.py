def _put_model(D, name, dat, m):
    try:
        _pc = m.group(1) + 'Data'
        _section = m.group(1) + m.group(2)
        if _pc not in D:
            print('{} not found in the provided dataset. Please try again'.
                format(_pc))
            return
        else:
            if _section not in D[_pc]:
                D[_pc][_section] = OrderedDict()
            if 'model' not in D[_pc][_section]:
                D[_pc][_section]['model'] = OrderedDict()
            if name not in D[_pc][_section]['model']:
                dat = _update_table_names(name, dat)
                D[_pc][_section]['model'][name] = dat
            else:
                _prompt_overwrite = input(
                    'This model already exists in the dataset. Do you want to overwrite it? (y/n)'
                    )
                if _prompt_overwrite == 'y':
                    dat = _update_table_names(name, dat)
                    D[_pc][_section]['model'][name] = dat
                elif _prompt_overwrite == 'n':
                    _name2 = _prompt_placement(D, 'model')
                    _m = re.match(re_model_name, _name2)
                    if _m:
                        D = _put_model(D, _name2, dat, _m)
                else:
                    print('Invalid choice')
    except Exception as e:
        print('addModel: Unable to put the model data into the dataset, {}'
            .format(e))
    return D