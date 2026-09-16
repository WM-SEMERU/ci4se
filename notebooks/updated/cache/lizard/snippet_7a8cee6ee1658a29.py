def get_discord_leaderboard(self, guild):
    r = requests.get(api_url + 'leaderboard/discord/' + str(guild) + '/',
        headers=self.headers)
    print(request_status(r))
    r.raise_for_status()
    return DiscordLeaderboard(r.json())