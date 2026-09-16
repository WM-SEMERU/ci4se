def print_prompt(prompt, msg_id=None):
    global show_execution_count
    if show_execution_count and msg_id:
        try:
            child = get_child_msg(msg_id)
            count = child['content']['execution_count']
            echo('In[%d]: %s' % (count, prompt))
        except Empty:
            echo('In[]: %s (no reply from IPython kernel)' % prompt)
    else:
        echo('In[]: %s' % prompt)