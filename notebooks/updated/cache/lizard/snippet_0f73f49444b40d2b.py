def plot_mask_cells(mask_cells, padding=16):
    fig, axes = plt.subplots(len(mask_cells), 3, figsize=(12, 10))
    for idx, (axes, mask_cell) in enumerate(zip(axes, mask_cells), 1):
        ax1, ax2, ax3 = axes
        true_mask, predicted_mask, cell = mask_cell
        plot_mask_cell(true_mask, predicted_mask, cell, 'Type {}'.format(
            idx), ax1, ax2, ax3, padding=padding)
    fig.tight_layout()
    return fig, axes