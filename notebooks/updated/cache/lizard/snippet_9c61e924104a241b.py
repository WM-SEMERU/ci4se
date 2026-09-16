def handle_menu_event(self, obj):
    menuitem = obj.menuitem
    if menuitem.returnkey.startswith('# '):
        cmd = menuitem.returnkey[2:]
        if menuitem.handler is not None:
            if menuitem.handler_result is None:
                return
            cmd += menuitem.handler_result
        self.mpstate.functions.process_stdin(cmd)
    elif menuitem.returnkey == 'popupRallyRemove':
        self.remove_rally(obj.selected[0].objkey)
    elif menuitem.returnkey == 'popupRallyMove':
        self.move_rally(obj.selected[0].objkey)
    elif menuitem.returnkey == 'popupMissionSet':
        self.set_mission(obj.selected[0].objkey, obj.selected[0].extra_info)
    elif menuitem.returnkey == 'popupMissionRemoveNoFly':
        self.remove_mission_nofly(obj.selected[0].objkey, obj.selected[0].
            extra_info)
    elif menuitem.returnkey == 'popupMissionRemove':
        self.remove_mission(obj.selected[0].objkey, obj.selected[0].extra_info)
    elif menuitem.returnkey == 'popupMissionMove':
        self.move_mission(obj.selected[0].objkey, obj.selected[0].extra_info)
    elif menuitem.returnkey == 'popupFenceRemove':
        self.remove_fencepoint(obj.selected[0].objkey, obj.selected[0].
            extra_info)
    elif menuitem.returnkey == 'popupFenceMove':
        self.move_fencepoint(obj.selected[0].objkey, obj.selected[0].extra_info
            )
    elif menuitem.returnkey == 'showPosition':
        self.show_position()