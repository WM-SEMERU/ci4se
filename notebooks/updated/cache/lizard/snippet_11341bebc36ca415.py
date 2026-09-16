def main():
    sandbox = create_sandbox()
    directory = download_package_to_sandbox(sandbox,
        'https://pypi.python.org/packages/source/c/checkmyreqs/checkmyreqs-0.1.6.tar.gz'
        )
    print(directory)
    destroy_sandbox(sandbox)