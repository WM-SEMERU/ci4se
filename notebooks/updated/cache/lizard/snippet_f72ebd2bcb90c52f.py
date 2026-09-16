def render_source(output_dir, package_spec):
    path, name = package_spec.filepath
    destination_filename = '%s/%s.h' % (output_dir, name)
    py_template = JENV.get_template(MESSAGES_TEMPLATE_NAME)
    with open(destination_filename, 'w') as f:
        f.write(py_template.render(msgs=package_spec.definitions, pkg_name=
            name, filepath='/'.join(package_spec.filepath) + '.yaml',
            max_msgid_len=package_spec.max_msgid_len, description=
            package_spec.description, timestamp=package_spec.
            creation_timestamp, include=extensions(package_spec.includes)))