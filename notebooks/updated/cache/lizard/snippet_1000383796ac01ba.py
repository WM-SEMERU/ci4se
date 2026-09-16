def muscle_seqs(seqs, add_seq_names=False, out_filename=None, input_handler
    =None, params={}, WorkingDir=tempfile.gettempdir(), SuppressStderr=None,
    SuppressStdout=None):
    if out_filename:
        params['-out'] = out_filename
    ih = input_handler or guess_input_handler(seqs, add_seq_names)
    muscle_app = Muscle(params=params, InputHandler=ih, WorkingDir=
        WorkingDir, SuppressStderr=SuppressStderr, SuppressStdout=
        SuppressStdout)
    return muscle_app(seqs)