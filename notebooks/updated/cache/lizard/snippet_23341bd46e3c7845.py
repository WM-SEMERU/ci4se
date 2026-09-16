def gpib_pass_control(library, session, primary_address, secondary_address):
    return library.viGpibPassControl(session, primary_address,
        secondary_address)