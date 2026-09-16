def unit(session):
    django_deps_27 = [('django==1.8.19',), ('django >= 1.11.0, < 2.0.0dev',)]
    if session.virtualenv.interpreter == '2.7':
        [default(session, django_dep=django) for django in django_deps_27]
    else:
        default(session)