def parse_site(sample, convention, Z):
    convention = str(convention)
    site = sample
    if convention == '1':
        return sample[:-1]
    if convention == '2':
        parts = sample.strip('-').split('-')
        return parts[0]
    if convention == '3':
        parts = sample.split('.')
        return parts[0]
    if convention == '4':
        k = int(Z) - 1
        return sample[0:-k]
    if convention == '5':
        return sample
    if convention == '6':
        print('-W- Finding names in orient.txt is not currently supported')
    if convention == '7':
        k = int(Z)
        return sample[0:k]
    if convention == '8':
        return ''
    if convention == '9':
        return sample
    print('Error in site parsing routine')
    return