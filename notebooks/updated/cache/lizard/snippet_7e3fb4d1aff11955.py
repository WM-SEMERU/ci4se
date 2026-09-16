def sorted_releases(self):
    releases = [(parse_version(release.version), release) for release in
        self.releases]
    releases.sort(reverse=True)
    return [release[1] for release in releases]