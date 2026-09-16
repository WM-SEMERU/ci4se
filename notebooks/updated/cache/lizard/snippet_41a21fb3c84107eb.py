def from_comm(cls, pub):
    filename = None
    if pub.b64_data:
        filename = cls._save_to_unique_filename(pub)
    return cls(isbn=pub.isbn, uuid=pub.uuid, aleph_id=pub.aleph_id,
        dir_pointer=filename)