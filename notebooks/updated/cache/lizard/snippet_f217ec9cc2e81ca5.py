def remove_extra_packages(self, packages, dry_run=False):
    removal_list = self.determine_extra_packages(packages)
    if not removal_list:
        print('No packages to be removed')
    elif dry_run:
        print('The following packages would be removed:\n    %s\n' %
            '\n    '.join(removal_list))
    else:
        print('Removing packages\n')
        args = ['pip', 'uninstall', '-y']
        args.extend(list(removal_list))
        subprocess.check_call(args)