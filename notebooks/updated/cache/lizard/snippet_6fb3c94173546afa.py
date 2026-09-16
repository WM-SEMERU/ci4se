async def jsk_git(self, ctx: commands.Context, *, argument: CodeblockConverter
    ):
    return await ctx.invoke(self.jsk_shell, argument=Codeblock(argument.
        language, 'git ' + argument.content))