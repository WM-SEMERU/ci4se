def generate_sibling_distance(self):
    sibling_distance = defaultdict(lambda : defaultdict(dict))
    topics = {p.topic for p in self.partitions}
    for source in self.brokers:
        for dest in self.brokers:
            if source != dest:
                for topic in topics:
                    sibling_distance[dest][source][topic
                        ] = dest.count_partitions(topic
                        ) - source.count_partitions(topic)
    return sibling_distance