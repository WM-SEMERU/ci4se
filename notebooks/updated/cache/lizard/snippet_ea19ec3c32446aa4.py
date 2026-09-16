def save_dataset(self, dataset, filename=None, fill_value=None, overlay=
    None, decorate=None, compute=True, **kwargs):
    img = get_enhanced_image(dataset.squeeze(), enhance=self.enhancer,
        overlay=overlay, decorate=decorate, fill_value=fill_value)
    return self.save_image(img, filename=filename, compute=compute,
        fill_value=fill_value, **kwargs)