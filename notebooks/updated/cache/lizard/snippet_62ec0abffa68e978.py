def create_tumor_bamdir(tumor, tumor_bam, normal_bam, work_dir):
    bam_dir = utils.safe_makedir(os.path.join(work_dir, tumor, 'in_bams'))
    normal_bam_ready = os.path.join(bam_dir, os.path.basename(normal_bam))
    utils.symlink_plus(normal_bam, normal_bam_ready)
    tumor_bam_ready = os.path.join(bam_dir, os.path.basename(tumor_bam))
    utils.symlink_plus(tumor_bam, tumor_bam_ready)
    return bam_dir, normal_bam_ready