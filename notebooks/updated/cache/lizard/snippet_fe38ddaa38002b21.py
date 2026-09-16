def multipart_uploadpart(self, multipart):
    (content_length, part_number, stream, content_type, content_md5, tags
        ) = current_files_rest.multipart_partfactory()
    if content_length:
        ck = (multipart.last_part_size if part_number == multipart.
            last_part_number else multipart.chunk_size)
        if ck != content_length:
            raise MultipartInvalidChunkSize()
    try:
        p = Part.get_or_create(multipart, part_number)
        p.set_contents(stream)
        db.session.commit()
    except Exception:
        db.session.rollback()
        Part.delete(multipart, part_number)
        raise
    return self.make_response(data=p, context={'class': Part}, etag=p.checksum)