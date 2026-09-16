def delete_with_casper_admin_save(self, pkg):
    if pkg.__class__.__name__ == 'Package':
        package_to_delete = pkg.id
    elif isinstance(pkg, int):
        package_to_delete = pkg
    elif isinstance(pkg, str):
        package_to_delete = self.connection['jss'].Package(pkg).id
    else:
        raise TypeError
    data_dict = {'username': self.connection['jss'].user, 'password': self.
        connection['jss'].password, 'deletedPackageID': package_to_delete}
    self.connection['jss'].session.post(url=self.connection['delete_url'],
        data=data_dict)