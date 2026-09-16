def check_global_status(flag, name, oid):
    if flag:
        myData = get_data(sess, oid, helper)
        data_summary_output, data_long_output = state_summary(myData, name,
            normal_state, helper)
        add_output(data_summary_output, data_long_output, helper)