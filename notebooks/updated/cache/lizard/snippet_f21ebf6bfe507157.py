def g_time_res(FlowPlant, IDTube, RadiusCoil, LengthTube, Temp):
    return g_coil(FlowPlant, IDTube, RadiusCoil, Temp
        ).magnitude * time_res_tube(IDTube, LengthTube, FlowPlant).magnitude