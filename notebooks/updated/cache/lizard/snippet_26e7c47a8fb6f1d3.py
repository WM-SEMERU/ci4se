def _collect_data(directory):
    data_files = []
    transcripts = [filename for filename in os.listdir(directory) if
        filename.endswith('.csv')]
    for transcript in transcripts:
        transcript_path = os.path.join(directory, transcript)
        with open(transcript_path, 'r') as transcript_file:
            transcript_reader = csv.reader(transcript_file)
            _ = next(transcript_reader)
            for transcript_line in transcript_reader:
                media_name, label = transcript_line[0:2]
                filename = os.path.join(directory, media_name)
                data_files.append((media_name, filename, label))
    return data_files