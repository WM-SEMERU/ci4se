def get_requirements():
    packages = []
    with open('requirements.txt', 'r') as req_doc:
        for package in req_doc:
            packages.append(package.replace('\n', ''))
    return packages