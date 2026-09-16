def download_models(self, uniprot_acc, outdir='', force_rerun=False):
    downloaded = []
    subset = self.get_models(uniprot_acc)
    for entry in subset:
        ident = '{}_{}_{}_{}'.format(uniprot_acc, entry['template'], entry[
            'from'], entry['to'])
        outfile = op.join(outdir, ident + '.pdb')
        if ssbio.utils.force_rerun(flag=force_rerun, outfile=outfile):
            response = requests.get(entry['url'])
            if response.status_code == 404:
                log.error('{}: 404 returned, no model available.'.format(ident)
                    )
            else:
                with open(outfile, 'w') as f:
                    f.write(response.text)
                log.debug('{}: downloaded homology model'.format(ident))
                downloaded.append(outfile)
        else:
            downloaded.append(outfile)
    return downloaded