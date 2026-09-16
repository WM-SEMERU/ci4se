def fromstring(cls, dis_string):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(dis_string)
    temp.close()
    dis_tree = cls(dis_filepath=temp.name)
    os.unlink(temp.name)
    return dis_tree