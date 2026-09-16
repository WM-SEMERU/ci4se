def generate_sample_json():
    check = EpubCheck(samples.EPUB3_VALID)
    with open(samples.RESULT_VALID, 'wb') as jsonfile:
        jsonfile.write(check._stdout)
    check = EpubCheck(samples.EPUB3_INVALID)
    with open(samples.RESULT_INVALID, 'wb') as jsonfile:
        jsonfile.write(check._stdout)