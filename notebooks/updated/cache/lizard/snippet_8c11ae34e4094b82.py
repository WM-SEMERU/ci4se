def setup_menus():
    menu = MPMenuTop([])
    menu.add(MPMenuSubMenu('MAVExplorer', items=[MPMenuItem('Settings',
        'Settings', 'menuSettings'), MPMenuItem('Map', 'Map', '# map'),
        MPMenuItem('Save Graph', 'Save', '# save'), MPMenuItem(
        'Reload Graphs', 'Reload', '# reload')]))
    menu.add(graph_menus())
    menu.add(MPMenuSubMenu('FlightMode', items=flightmode_menu()))
    mestate.console.set_menu(menu, menu_callback)