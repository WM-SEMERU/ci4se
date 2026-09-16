def do_notification_show(mc, args):
    fields = {}
    fields['notification_id'] = args.id
    try:
        notification = mc.notifications.get(**fields)
    except (osc_exc.ClientException, k_exc.HttpError) as he:
        raise osc_exc.CommandError('%s\n%s' % (he.message, he.details))
    else:
        if args.json:
            print(utils.json_formatter(notification))
            return
        formatters = {'name': utils.json_formatter, 'id': utils.
            json_formatter, 'type': utils.json_formatter, 'address': utils.
            json_formatter, 'period': utils.json_formatter, 'links': utils.
            format_dictlist}
        utils.print_dict(notification, formatters=formatters)