def get_leaderboard(self, app_id, name):
    message = MsgProto(EMsg.ClientLBSFindOrCreateLB)
    message.header.routing_appid = app_id
    message.body.app_id = app_id
    message.body.leaderboard_name = name
    message.body.create_if_not_found = False
    resp = self.send_job_and_wait(message, timeout=15)
    if not resp:
        raise LookupError("Didn't receive response within 15seconds :(")
    if resp.eresult != EResult.OK:
        raise LookupError(EResult(resp.eresult))
    return SteamLeaderboard(self, app_id, name, resp)