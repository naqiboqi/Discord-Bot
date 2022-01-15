import re

from random import randint
from discord import Embed, Color
from discord.ext import commands

from constants import diceDict

##---------------------------------------------------------------

class RollTypes(commands.Cog):
    def __init__(self, final_roll):
        self.final_roll = final_roll
        
    
    async def printRoll(self, ctx: commands.Context):
        
        embed = Embed(title = 'amogus', 
        description = (self.final_roll))
        await ctx.send(embed = embed)
        
    
    @commands.command(name = 'ability')
    async def abilityRoll(self, ctx: commands.Context):
        """Does a standard ability roll (4d6 and drop lowest)
        
        """
        
        ab_list, temp = [], []
        times = 4
        sides = 6

        for roll in range(times):
            ab_roll = randint(1, sides)
            ab_list.append(ab_roll)
            temp.append(ab_roll)

        ab_list.remove(min(ab_list))
        final_roll = sum(ab_list)

        die_art = diceDict.die_images[sides]
        types = 'ability'
    
        embed = Embed(title = (F'Rolling {types}'), 
        description = (F'```\n{die_art}\n```\n\nRolled {temp} {types} for {final_roll}!'), color = Color.blue())
        await ctx.send(embed = embed)
        
    @commands.command(name = 'highroll')
    async def advantageRoll(self, ctx:commands.Context):
        """Rolls 2d20 for advantage (higher roll)
        
        """
        
        times = 2
        sides = 20
        results = []

        for roll in range(times):
            new_roll = randint(1, sides)
            results.append(new_roll)
            
        final_roll = max(results)
        
        die_art = diceDict.die_images[sides]
        types = 'for advantage'
    
        embed = Embed(title = (F'Rolling {types}'), 
        description = (F'```\n{die_art}\n```\n\nRolled {results} {types} for {final_roll}!'), color = Color.blue())
        await ctx.send(embed = embed)
    
        
    @commands.command(name = 'lowroll')
    async def disadvantageRoll(self, ctx: commands.Context):
        """Rolls 2d20 for disadvantage (lower roll)
        
        """
        
        times = 2
        sides = 20
        results = []
        types = 'for disadvantage'
        
        for rolls in range(times):
            new_roll = randint(1, sides)
            results.append(new_roll)
            
        final_roll = min(results)
        die_art = diceDict.die_images[sides]
        
        embed = Embed(title = (F'Rolling {types}'), 
        description = (F'```\n{die_art}\n```\n\nRolled {results} {types} for {final_roll}!'), color = Color.blue())
        await ctx.send(embed = embed)
    
    
    @commands.command(name = 'roll')
    async def standardRoll(self, ctx: commands.Context):
        """Does a standard roll: 4d6 --> Rolls a six sided die four times
        
        """
        try:
            roll_choice = ctx.message.content
            
            if re.match("![a-z]+ [\d]+d[\d]+", roll_choice):
                roll_numbers = re.findall(r'\d+', roll_choice)
                times, sides = int(roll_numbers[0]), int(roll_numbers[1])
                types = 'standard'
                
                results = []
                for roll_count in range(times):
                    dice_roll = randint(1, sides)
                    results.append(dice_roll)
    
                final_roll = max(results)
                die_art = diceDict.die_images[sides]
    
                embed = Embed(title = (F'Rolling {types}'), 
                description = (F'```\n{die_art}\n```\n\nRolled {results} {types} for {final_roll}!'), color = Color.blue())
                await ctx.send(embed = embed)
    
        except:
            return
        

def setup(bot: commands.Bot):
    bot.add_cog(RollTypes(bot))