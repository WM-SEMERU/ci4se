def plot_mask_cell(true_mask, predicted_mask, cell, suffix, ax1, ax2, ax3,
    padding=16):
    for ax in [ax1, ax2, ax3]:
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
    ax1.imshow(true_mask[padding:-padding, padding:-padding], cmap='viridis')
    ax1.set_title('True Mask - {}'.format(suffix))
    ax2.imshow(predicted_mask[padding:-padding, padding:-padding], cmap=
        'viridis')
    ax2.set_title('Predicted Mask - {}'.format(suffix))
    ax3.imshow(convert_cell_to_img(cell, padding=padding))
    ax3.set_title('Image - {}'.format(suffix))
    return ax1, ax2, ax3