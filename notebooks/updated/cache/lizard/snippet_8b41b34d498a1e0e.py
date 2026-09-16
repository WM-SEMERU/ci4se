def show_highstate(**kwargs):
    __opts__['grains'] = __grains__
    opts = salt.utils.state.get_sls_opts(__opts__, **kwargs)
    st_ = salt.client.ssh.state.SSHHighState(opts, __pillar__, __salt__,
        __context__['fileclient'])
    st_.push_active()
    chunks = st_.compile_highstate()
    _cleanup_slsmod_high_data(chunks)
    return chunks