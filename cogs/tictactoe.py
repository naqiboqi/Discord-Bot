from discord.ext import commands

class TicTacToe(commands.Cog):
    pass



def setup(bot: commands.Bot):
    bot.add_cog(TicTacToe(bot))