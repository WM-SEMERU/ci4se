def add_case():
    ind_ids = request.form.getlist('ind_id')
    case_id = request.form['case_id']
    source = request.form['source']
    variant_type = request.form['type']
    if len(ind_ids) == 0:
        return abort(400, 'must add at least one member of case')
    new_case = Case(case_id=case_id, name=case_id, variant_source=source,
        variant_type=variant_type, variant_mode='gemini')
    for ind_id in ind_ids:
        ind_obj = app.db.individual(ind_id)
        new_case.individuals.append(ind_obj)
    app.db.session.add(new_case)
    app.db.save()
    return redirect(url_for('.case', case_id=new_case.name))