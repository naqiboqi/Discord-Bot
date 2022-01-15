import discord
import json
import datetime

from asyncio import sleep
from discord.ext import commands
from random import choice

from discord.ext.commands.errors import MemberNotFound

class AbyssBar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                    
        self.specials = {
                'Backbreaker Stout' : 1, 'Dark Morkite' : 2,
                "Pots O' Gold" : 3, 'Red Rock Blaster' : 1,
                'Rocky Mountain' : 3, 'Skull Crusher Ale': 2,
                'Slayer Stout' : 2, 'Tunnel Rat' : 3
                }
        
        self.corporate = {
                'Oily Oaf Brew' : (35, 'Credits'), 'Glyphid Slammer' : (85, 'Credits'), 
                "Leaf Lover's Special" : (25, 'Credits')
                }
    
        self.sfw = {
                'Arkenstout' : (4, 'Malt Star'), 'Seasoned Moonrider' : (4, 'Starch Nut')
                }
        
        self.regular = {
                'Blackreach Blonde' : (3, 'Yeast Cone'), 'Burning Love' : (6, 'Malt Star'),
                'Underhill Deluxe' : (4, 'Yeast Cone')
                }
                
        self.strong = {
                "Flintlocke's Delight" : (2, 'Starch Nut'), 'Malt Rockbearer' : (6, 'Yeast Cone'),
                'Smart Stout' : (4, 'Malt Star'), 'Wormhole Special' : (3, 'Starch Nut')
                }
        
        self.epic = {
                'Blackrock Lager' : (5, 'Starch Nut'), 'Gut Wrecker' : (4, 'Starch Nut'),
                'Mactera Brew' : (6, 'Starch Nut')
                }
        
        self.legendary = {
                'Blackout Stout' : (3, 'Starch Nut')
                }

        self.beers = [self.corporate, self.sfw, self.regular, self.strong, self.epic, self.legendary]
        
        try:
            with open('bank.json') as file:
                self.balances = json.load(file)
            
        except:
            print('Could not load bank.json')
            self.balances = {}
            
    @commands.command(name = 'showmenu')
    async def showBeers(self, ctx: commands.Context):   
        """The finest beers, offered only at the Abyss Bar!
        
        """
        
        embed = discord.Embed(title = 'The Abyss Bar\n' + '-' * 50,
        description = (F"The finest beers in the galaxy\n\nTODAY'S SPECIAL: \n<:drgpickaxe:920880811497119794> "))

        for dict_item in self.beers:
            beers, prices = '', ''
            for key in dict_item:
                beers += key + '\n'
                prices += str(dict_item[key][0]) + ' ' + dict_item[key][1] + '\n'
                
            newlines = beers.count('\n') + 1

            embed.add_field(name = 'Beer', value = beers, inline =  True)
            embed.add_field(name = 'Prices', value = prices, inline = True)
            embed.add_field(name = '|', value = ('|' + '\n') * newlines, inline = True)
        
        await ctx.send(embed = embed)
        
        
    @commands.command(name = 'order')
    async def orderBeer(self, ctx: commands.Context):
        """Orders a hearty beer! Don't forget to tip
        
        """
        user_order = ctx.message.content[7:]
        for dict_item in self.beers:
            for key in dict_item:
                if user_order.lower() == key.lower():
                
                    await ctx.send(F'Pouring a delicious {key}...')
                    await sleep(1)
                    await ctx.send(F'Enjoy your drink! Rock and Stone!  <:drgpickaxe:920880811497119794>')
                    return
                
        
    @commands.command(name = 'tip')
    async def tipBosco(self, ctx: commands.Context):
        """Tips our good ol' boy Bosco
        
        """
        id = ctx.message.author.id
        
        if str(id) in self.balances:
            self.balances[str(id)] -= 5
            AbyssBar._save(self)
            
            
        await ctx.send('Your tip is appreciated. Rock and Stone!')
        
        
    @commands.command(name = 'balance')
    async def playerBalance(self, ctx: commands.Context):
        id = ctx.message.author.id
        
        if str(id) in self.balances:
            await ctx.send(F'You have {self.balances[str(id)]} credits in the bank')
            
        else:
            await ctx.send("You're not a member of the union... why not join?")
            return
            
            
    @commands.command(name = 'register')
    async def playerRegister(self, ctx: commands.Context):
        id = ctx.message.author.id
        
        if str(id) in self.balances:
            await ctx.send("You're already registered. Why don't you get to work?")
    
        else:
            self.balances[id] = 200
            AbyssBar._save(self)
            await ctx.send('Congratulations on signing on for Deep Rock Galactic, miner, and welcome on board. Rock and Stone! <:drgpickaxe:920880811497119794>')
    
    
    @commands.command(name = 'transfer')
    async def transferCredits(self, ctx: commands.Context, other: discord.Member, amount: int):
        try:
            giver_id = ctx.message.author.id
            recieve_mention_id = other.id
            
            print(str(giver_id))
            print(str(recieve_mention_id))
            
        except MemberNotFound:
            await ctx.send("Can't find that member. Use mentions")
            
        if str(giver_id) not in self.balances:
            await ctx.send('You are not registered in the union!')
            
        elif amount <= 0:
            await ctx.send("Can only send a positive amount!")
            
        elif str(recieve_mention_id) not in self.balances:
            await ctx.send('The other party is not part of the union!')
            
        elif giver_id == recieve_mention_id:
            await ctx.send('Transferring credits to yourself, kinda sus bro')
            
        elif self.balances[str(giver_id)] < amount:
            await ctx.send("You don't have enough credits!")
            
        else:
            self.balances[str(giver_id)] -= amount
            self.balances[str(recieve_mention_id)] += amount
            
            await ctx.send(F'Successfully transfered {amount} credits to {other}')
            AbyssBar._save(self)
        
    
    def _save(self):
        with open('bank.json', 'w') as file:
            json.dump(self.balances, file)
            print(self.balances)
            print('Saved to bank.json!')
        
        
def setup(bot: commands.Bot):
    bot.add_cog(AbyssBar(bot))