def clean_download_cache(self, args):
    ctx = self.ctx
    if hasattr(args, 'recipes') and args.recipes:
        for package in args.recipes:
            remove_path = join(ctx.packages_path, package)
            if exists(remove_path):
                shutil.rmtree(remove_path)
                info('Download cache removed for: "{}"'.format(package))
            else:
                warning('No download cache found for "{}", skipping'.format
                    (package))
    elif exists(ctx.packages_path):
        shutil.rmtree(ctx.packages_path)
        info('Download cache removed.')
    else:
        print('No cache found at "{}"'.format(ctx.packages_path))