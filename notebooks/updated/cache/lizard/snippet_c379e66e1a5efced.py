def ynbox(msg='Shall I continue?', title=' ', choices=('[<F1>]Yes',
    '[<F2>]No'), image=None, default_choice='[<F1>]Yes', cancel_choice=
    '[<F2>]No'):
    return boolbox(msg=msg, title=title, choices=choices, image=image,
        default_choice=default_choice, cancel_choice=cancel_choice)