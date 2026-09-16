def _do_config_proposal_list(args):

    def _accept(candidate, public_key, prefix):
        has_pub_key = not public_key or candidate.votes[0
            ].public_key == public_key
        has_prefix = candidate.proposal.setting.startswith(prefix)
        return has_prefix and has_pub_key
    candidates_payload = _get_proposals(RestClient(args.url))
    candidates = [c for c in candidates_payload.candidates if _accept(c,
        args.public_key, args.filter)]
    if args.format == 'default':
        for candidate in candidates:
            print('{}: {} => {}'.format(candidate.proposal_id, candidate.
                proposal.setting, candidate.proposal.value))
    elif args.format == 'csv':
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(['PROPOSAL_ID', 'KEY', 'VALUE'])
        for candidate in candidates:
            writer.writerow([candidate.proposal_id, candidate.proposal.
                setting, candidate.proposal.value])
    elif args.format == 'json' or args.format == 'yaml':
        candidates_snapshot = {c.proposal_id: {c.proposal.setting: c.
            proposal.value} for c in candidates}
        if args.format == 'json':
            print(json.dumps(candidates_snapshot, indent=2, sort_keys=True))
        else:
            print(yaml.dump(candidates_snapshot, default_flow_style=False)[
                0:-1])
    else:
        raise AssertionError('Unknown format {}'.format(args.format))