def regex_in_file(regex, filepath, return_match=False):
    file_content = get_file_content(filepath)
    re_method = funcy.re_find if return_match else funcy.re_test
    return re_method(regex, file_content)