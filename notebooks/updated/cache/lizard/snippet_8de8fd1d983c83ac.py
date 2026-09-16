def delete(stack_ref: List[str], region: str, dry_run: bool, force: bool,
    remote: str):
    lizzy = setup_lizzy_client(remote)
    stack_refs = get_stack_refs(stack_ref)
    all_with_version = all(stack.version is not None for stack in stack_refs)
    if not all_with_version and not dry_run and not force:
        fatal_error('Error: {} matching stacks found. '.format(len(
            stack_refs)) +
            'Please use the "--force" flag if you really want to delete multiple stacks.'
            )
    output = ''
    for stack in stack_refs:
        if stack.version is not None:
            stack_id = '{stack.name}-{stack.version}'.format(stack=stack)
        else:
            stack_id = stack.name
        with Action("Requesting stack '{stack_id}' deletion..", stack_id=
            stack_id):
            output = lizzy.delete(stack_id, region=region, dry_run=dry_run)
    print(output)