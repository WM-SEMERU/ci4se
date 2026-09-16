def GameTypeEnum(ctx):
    return Enum(ctx, RM=0, Regicide=1, DM=2, Scenario=3, Campaign=4,
        KingOfTheHill=5, WonderRace=6, DefendTheWonder=7, TurboRandom=8)