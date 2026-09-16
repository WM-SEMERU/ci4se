def organize_models(self, outdir, force_rerun=False):
    uniprot_to_swissmodel = defaultdict(list)
    for u, models in self.all_models.items():
        for m in models:
            original_filename = '{}_{}_{}_{}'.format(m['from'], m['to'], m[
                'template'], m['coordinate_id'])
            file_path = op.join(self.metadata_dir, u[:2], u[2:4], u[4:],
                'swissmodel', '{}.pdb'.format(original_filename))
            if op.exists(file_path):
                new_filename = '{}_{}_{}_{}.pdb'.format(u, m['from'], m[
                    'to'], m['template'][:4])
                shutil.copy(file_path, op.join(outdir, new_filename))
                uniprot_to_swissmodel[u].append(new_filename)
            else:
                log.warning('{}: no file {} found for model'.format(u,
                    file_path))
    return uniprot_to_swissmodel