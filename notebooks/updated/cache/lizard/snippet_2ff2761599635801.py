def fmt_account(account, title=None):
    if title is None:
        title = account.__class__.__name__
    title = '{} ({} causal link{})'.format(title, len(account), '' if len(
        account) == 1 else 's')
    body = ''
    body += 'Irreducible effects\n'
    body += '\n'.join(fmt_ac_ria(m) for m in account.irreducible_effects)
    body += '\nIrreducible causes\n'
    body += '\n'.join(fmt_ac_ria(m) for m in account.irreducible_causes)
    return '\n' + header(title, body, under_char='*')