def get_image(self, path):
    image = ''
    name = os.path.basename(path)
    if not StockImage.is_registered(name):
        ipath = self.__find_image(path)
        if ipath is not None:
            StockImage.register(name, ipath)
        else:
            msg = "Image '{0}' not found in resource paths.".format(name)
            logger.warning(msg)
    try:
        image = StockImage.get(name)
    except StockImageException:
        pass
    return image