def _get_possible_sequences(cls, mode, length, date_style):
    sequences = []
    date_sequences = (cls.DATE_SEQUENCES_DAY_FIRST if date_style ==
        DateStyle.DAY_FIRST else cls.DATE_SEQUENCES_MONTH_FIRST)
    if mode == Mode.DATE or mode == Mode.AUTO:
        for seq in date_sequences:
            if len(seq) == length:
                sequences.append(seq)
    elif mode == Mode.TIME:
        for seq in cls.TIME_SEQUENCES:
            if len(seq) == length:
                sequences.append(seq)
    if mode == Mode.DATETIME or mode == Mode.AUTO:
        for date_seq in date_sequences:
            for time_seq in cls.TIME_SEQUENCES:
                if len(date_seq) + len(time_seq) == length:
                    sequences.append(date_seq + time_seq)
    return sequences