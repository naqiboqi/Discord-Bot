from random import randint
from discord.ext import commands

class RockPaperScissors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ROCK, self.PAPER, self.SCISSORS = 0, 1, 2
    
        self.actions = ["smashes", "smothers", "slices"]
        self.win_cond = [(self.ROCK, self.SCISSORS), (self.PAPER, self.ROCK), (self.SCISSORS, self.PAPER)]
        
        self.user_input_dict = {
        'rock': self.ROCK, 'paper': self.PAPER, 'scissors': self.SCISSORS
        }
        
        self.winner_results = ('rock', 'paper', 'scissors')
        self.winner_emojis = (':rock:', ':roll_of_paper:', ':scissors:')
    
    @commands.command(name = 'rps')
    async def rockPaperScissors(self, ctx: commands.Context):
        """A true test of skill. (!rps rock, !rps paper, !rps scissors)
        
        """
        
        get_message = ctx.message.content[5:]
        user_choice = self.user_input_dict.get(get_message)
        comp_choice = randint(0, 2)
        
        if get_message not in self.winner_results:
            await ctx.send('Please choose rock, paper, or scissors')
            return
        
        await ctx.send(F'I choose {self.winner_emojis[comp_choice]}')
        
        if user_choice == comp_choice:
            await ctx.send(F'A tie! :thinking:')
            
        else:
            user_wins = (user_choice, comp_choice) in self.win_cond
            winner, loser = (user_choice, comp_choice) if user_wins else (comp_choice, user_choice)
            
            if user_wins:
                win_or_lose = 'win'
                
            else:
                win_or_lose = 'lose'
                
            await ctx.send(F"You {win_or_lose}! - {self.winner_emojis[winner]} {self.actions[winner]} {self.winner_emojis[loser]}")
            
            
def setup(bot):
    bot.add_cog(RockPaperScissors(bot))