def dimensions_wizard():
    option = yield MultipleChoice('What type of SpiNNaker system to you have?',
        ["A single four-chip 'SpiNN-3' board",
        "A single forty-eight-chip 'SpiNN-5' board",
        "Multiple forty-eight-chip 'SpiNN-5' boards", 'Other'], None)
    assert 0 <= option < 4
    if option == 0:
        raise Success({'dimensions': (2, 2)})
    elif option == 1:
        raise Success({'dimensions': (8, 8)})
    elif option == 2:
        num_boards = yield Text("How many 'SpiNN-5' boards are in the system?")
        try:
            w, h = standard_system_dimensions(int(num_boards))
        except ValueError:
            raise Failure("'{}' is not a valid number of boards.".format(
                num_boards))
        raise Success({'dimensions': (w, h)})
    else:
        dimensions = yield Text(
            'What are the dimensions of the network in chips (e.g. 24x12)?')
        match = re.match('\\s*(\\d+)\\s*[xX]\\s*(\\d+)\\s*', dimensions)
        if not match:
            raise Failure("'{}' is not a valid system size.".format(dimensions)
                )
        else:
            w = int(match.group(1))
            h = int(match.group(2))
            raise Success({'dimensions': (w, h)})