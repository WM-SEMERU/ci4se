def save(self, output_path=None, title=None):
    try:
        save_figure(self.fig, output_path=output_path, annot=title)
    except:
        print('Unable to save the figure to disk! \nException: ')
        traceback.print_exc()