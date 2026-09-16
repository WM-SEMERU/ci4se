def main():
    parser = argparse.ArgumentParser(description='Convert ULog to KML')
    parser.add_argument('filename', metavar='file.ulg', help='ULog input file')
    parser.add_argument('-o', '--output', dest='output_filename', help=
        'output filename', default='track.kml')
    parser.add_argument('--topic', dest='topic_name', help=
        'topic name with position data (default=vehicle_gps_position)',
        default='vehicle_gps_position')
    parser.add_argument('--camera-trigger', dest='camera_trigger', help=
        'Camera trigger topic name (e.g. camera_capture)', default=None)
    args = parser.parse_args()
    convert_ulog2kml(args.filename, args.output_filename,
        position_topic_name=args.topic_name, camera_trigger_topic_name=args
        .camera_trigger)