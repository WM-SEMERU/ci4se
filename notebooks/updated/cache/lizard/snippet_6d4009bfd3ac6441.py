def get_stats(self):
    try:
        ret = fcntl.ioctl(self.ins, BIOCGSTATS, struct.pack('2I', 0, 0))
        return struct.unpack('2I', ret)
    except IOError:
        warning('Unable to get stats from BPF !')
        return None, None