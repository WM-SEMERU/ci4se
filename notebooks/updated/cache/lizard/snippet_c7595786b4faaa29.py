def new(cls, connection, segments=()):
    return cls(connection.session_id, connection.get_next_packet_count(),
        segments, autocommit=connection.autocommit)