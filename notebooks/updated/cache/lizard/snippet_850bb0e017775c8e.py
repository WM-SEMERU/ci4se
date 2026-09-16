def _array_safe_dict_eq(one_dict, other_dict):
    for key in one_dict:
        try:
            assert one_dict[key] == other_dict[key]
        except ValueError as err:
            if isinstance(one_dict[key], dict):
                assert FitResults._array_safe_dict_eq(one_dict[key],
                    other_dict[key])
            else:
                assert np.allclose(one_dict[key], other_dict[key])
        except AssertionError:
            return False
    else:
        return True