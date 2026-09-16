def __update_keyboard(self, milliseconds):
    if Ragnarok.get_world().Keyboard.is_clicked(self.move_up_button):
        self.move_up()
    elif Ragnarok.get_world().Keyboard.is_clicked(self.move_down_button):
        self.move_down()
    elif Ragnarok.get_world().Keyboard.is_clicked(self.select_button):
        self.gui_buttons[self.current_index].clicked_action()
    for button in self.gui_buttons:
        button.update(milliseconds)