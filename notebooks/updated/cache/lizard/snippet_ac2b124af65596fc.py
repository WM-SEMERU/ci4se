def body(self, frame):
    master = Frame(self)
    master.pack(padx=5, pady=0, expand=1, fill=BOTH)
    title = Label(master, text='Buses')
    title.pack(side=TOP)
    bus_lb = self.bus_lb = Listbox(master, selectmode=SINGLE, width=10)
    bus_lb.pack(side=LEFT)
    for bus in self.case.buses:
        bus_lb.insert(END, bus.name)
    bus_lb.bind('<<ListboxSelect>>', self.on_bus)
    self.bus_params = BusProperties(master)
    return bus_lb