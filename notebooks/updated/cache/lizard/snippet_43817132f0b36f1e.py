def add_menu(self, menu):
    from MAVProxy.modules.mavproxy_map import mp_slipmap
    self.default_popup.add(menu)
    self.map.add_object(mp_slipmap.SlipDefaultPopup(self.default_popup,
        combine=True))