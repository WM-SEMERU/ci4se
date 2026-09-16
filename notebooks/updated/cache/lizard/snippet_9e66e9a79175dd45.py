def find_view_menu(self, name):
    return self.get_session.query(self.viewmenu_model).filter_by(name=name
        ).first()