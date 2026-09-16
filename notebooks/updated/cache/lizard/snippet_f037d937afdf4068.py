def prompt_save_images(args):
    if args['images'] or args['no_images']:
        return
    if (args['pdf'] or args['html']) and (args['crawl'] or args['crawl_all']):
        save_msg = """Choosing to save images will greatly slow the crawling process.
Save images anyways? (y/n): """
        try:
            save_images = utils.confirm_input(input(save_msg))
        except (KeyboardInterrupt, EOFError):
            return
        args['images'] = save_images
        args['no_images'] = not save_images