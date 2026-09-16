def main():
    args = parse_arguments()
    if args.key is None:
        print('Error: Must provide IFTTT secret key.')
        sys.exit(1)
    try:
        res = pyfttt.send_event(api_key=args.key, event=args.event, value1=
            args.value1, value2=args.value2, value3=args.value3)
    except requests.exceptions.ConnectionError:
        print('Error: Could not connect to IFTTT')
        sys.exit(2)
    except requests.exceptions.HTTPError:
        print('Error: Received invalid response')
        sys.exit(3)
    except requests.exceptions.Timeout:
        print('Error: Request timed out')
        sys.exit(4)
    except requests.exceptions.TooManyRedirects:
        print('Error: Too many redirects')
        sys.exit(5)
    except requests.exceptions.RequestException as reqe:
        print('Error: {e}'.format(e=reqe))
        sys.exit(6)
    if res.status_code != requests.codes.ok:
        try:
            j = res.json()
        except ValueError:
            print('Error: Could not parse server response. Event not sent')
            sys.exit(7)
        for err in j['errors']:
            print('Error: {}'.format(err['message']))
        sys.exit(8)