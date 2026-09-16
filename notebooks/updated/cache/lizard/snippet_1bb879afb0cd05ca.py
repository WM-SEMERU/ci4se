def compute_video_metrics_from_predictions(predictions, decode_hparams):
    all_results = {}
    ssim_all_decodes, psnr_all_decodes = [], []
    for single_decode in predictions:
        args = get_zipped_dataset_from_predictions(single_decode)
        psnr_single, ssim_single = compute_one_decoding_video_metrics(*args)
        psnr_all_decodes.append(psnr_single)
        ssim_all_decodes.append(ssim_single)
    psnr_all_decodes = np.array(psnr_all_decodes)
    ssim_all_decodes = np.array(ssim_all_decodes)
    all_results.update({'PSNR': psnr_all_decodes, 'SSIM': ssim_all_decodes})
    return compute_all_metrics_statistics(all_results)