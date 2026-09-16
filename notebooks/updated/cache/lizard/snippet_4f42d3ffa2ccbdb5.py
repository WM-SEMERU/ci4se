def _get_current_migration_state(self, loader, apps):
    apps = set(apps)
    relevant_applied = [migration for migration in loader.
        applied_migrations if migration[0] in apps]
    most_recents = dict(sorted(relevant_applied, key=lambda m: m[1]))
    most_recents = [[app, 'zero' if app not in most_recents else str(
        most_recents[app])] for app in apps]
    return most_recents