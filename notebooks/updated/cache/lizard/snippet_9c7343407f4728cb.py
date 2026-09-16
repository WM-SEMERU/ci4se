def download_needed(self, response, outfile, quiet=True):
    try:
        remote_date = datetime.strptime(response.headers['Last-Modified'],
            '%a, %d %b %Y %X %Z')
        if isfile(outfile):
            local_date = datetime.fromtimestamp(os.path.getmtime(outfile))
            if remote_date <= local_date:
                if not quiet:
                    print(os.path.basename(outfile) +
                        ': Skipping, found more recently modified local copy (use --force to force download)'
                        )
                return False
    except:
        pass
    return True