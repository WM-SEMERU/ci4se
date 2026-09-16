def new_program(self, _id, series, title, subtitle, description, mpaaRating,
    starRating, runTime, year, showType, colorCode, originalAirDate,
    syndicatedEpisodeNumber, advisories):
    if self.__v_program:
        print(
            '[Program: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s]'
             % (_id, series, title, subtitle, description, mpaaRating,
            starRating, runTime, year, showType, colorCode, originalAirDate,
            syndicatedEpisodeNumber, advisories))