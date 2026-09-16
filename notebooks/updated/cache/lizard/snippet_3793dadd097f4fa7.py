def add_output(summary_output, long_output, helper):
    if summary_output != '':
        helper.add_summary(summary_output)
    helper.add_long_output(long_output)