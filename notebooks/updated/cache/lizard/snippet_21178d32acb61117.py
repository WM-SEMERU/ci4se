def fromstring(cls, ptb_string, namespace='ptb', precedence=False,
    ignore_traces=True):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(ptb_string)
    temp.close()
    ptb_docgraph = cls(ptb_filepath=temp.name, namespace=namespace,
        precedence=precedence, ignore_traces=ignore_traces)
    os.unlink(temp.name)
    return ptb_docgraph