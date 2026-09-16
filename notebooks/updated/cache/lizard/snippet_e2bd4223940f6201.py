def delete_empty_children(self):
    for child in self.children:
        child.delete_empty_children()
        try:
            if os.path.exists(child.full_path):
                os.rmdir(child.full_path)
        except OSError:
            pass
        else:
            self.children.remove(child)