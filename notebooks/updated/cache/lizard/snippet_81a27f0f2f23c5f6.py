def cleanup_candidates(self, node_ip):
    if node_ip in self.factory.candidates:
        old_candidates = []
        for candidate in self.factory.candidates[node_ip]:
            elapsed = int(time.time() - candidate['time'])
            if elapsed > self.challege_timeout:
                old_candidates.append(candidate)
        for candidate in old_candidates:
            self.factory.candidates[node_ip].remove(candidate)