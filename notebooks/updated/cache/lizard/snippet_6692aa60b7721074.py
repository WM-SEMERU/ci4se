def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--password', type=str)
    parser.add_argument('--token', type=str)
    args = parser.parse_args()
    if not args.password and not args.token:
        print('password or token is required')
        exit(1)
    example(args.host, args.user, args.password, args.token)