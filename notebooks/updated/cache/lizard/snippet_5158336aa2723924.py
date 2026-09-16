def learn_transportation_mode(track, clf):
    for segment in track.segments:
        tmodes = segment.transportation_modes
        points = segment.points
        features = []
        labels = []
        for tmode in tmodes:
            points_part = points[tmode['from']:tmode['to']]
            if len(points_part) > 0:
                features.append(extract_features_2(points_part))
                labels.append(tmode['label'])
        clf.learn(features, labels)