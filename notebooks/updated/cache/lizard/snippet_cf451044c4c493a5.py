def save_plots(self, directory, format='png', recommended_only=False):
    for i, session in enumerate(self):
        session.save_plots(directory, prefix=str(i), format=format,
            recommended_only=recommended_only)