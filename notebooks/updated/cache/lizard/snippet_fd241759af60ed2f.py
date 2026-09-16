def show_all(key):

    def func(request, abbr, session, bill_id, key):
        fixed_bill_id = fix_bill_id(bill_id)
        if fixed_bill_id.replace(' ', '') != bill_id:
            return redirect('bill', abbr=abbr, session=session, bill_id=
                fixed_bill_id.replace(' ', ''))
        bill = db.bills.find_one({settings.LEVEL_FIELD: abbr, 'session':
            session, 'bill_id': fixed_bill_id})
        if bill is None:
            raise Http404('no bill found {0} {1} {2}'.format(abbr, session,
                bill_id))
        return render(request, templatename('bill_all_%s' % key), dict(abbr
            =abbr, metadata=Metadata.get_object(abbr), bill=bill, sources=
            bill['sources'], nav_active='bills'))
    return func