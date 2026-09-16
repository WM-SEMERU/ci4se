def add_cog(self, cog):
    if not isinstance(cog, Cog):
        raise TypeError('cogs must derive from Cog')
    cog = cog._inject(self)
    self.__cogs[cog.__cog_name__] = cog