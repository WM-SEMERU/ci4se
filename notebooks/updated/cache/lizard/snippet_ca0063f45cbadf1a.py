def start_end_from_segments(segment_file):
    from glue.ligolw.ligolw import LIGOLWContentHandler as h
    lsctables.use_in(h)
    indoc = ligolw_utils.load_filename(segment_file, False, contenthandler=h)
    segment_table = table.get_table(indoc, lsctables.SegmentTable.tableName)
    start = numpy.array(segment_table.getColumnByName('start_time'))
    start_ns = numpy.array(segment_table.getColumnByName('start_time_ns'))
    end = numpy.array(segment_table.getColumnByName('end_time'))
    end_ns = numpy.array(segment_table.getColumnByName('end_time_ns'))
    return start + start_ns * 1e-09, end + end_ns * 1e-09