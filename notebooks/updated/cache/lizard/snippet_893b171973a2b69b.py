def rst_to_pypi(contents):
    contents = contents.replace('.svg?pypi=png.from.svg', '.png')
    asterisks_length = len(PackageHelper.get_name())
    asterisks = '*' * asterisks_length
    title = asterisks + '\n' + PackageHelper.get_name() + '\n' + asterisks
    contents = re.sub(
        '(\\.\\. raw\\:\\: html\\n)(\\n {2,4})(\\<br class=\\"title\\"\\>)',
        title, contents)
    contents = re.sub(
        '(\\.\\. raw\\:\\: html\\n)((\\n {2,4})([A-Za-z0-9<>\\ =\\"\\/])*)*',
        '', contents)
    return contents