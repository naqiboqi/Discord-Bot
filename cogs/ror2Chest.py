import json

from discord import Embed
from discord.ext import commands
from random import choice, randint

class RandomStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'rainchest')
    async def rollROR2(self, ctx: commands.Context):
        """Rolls a medium ROR2 chest for items!
        
           You recieved Personal Shield Generator!
        
        """
        
        commons = ['Armor Piercing Rounds', 'Backup Magazine', 'Bison Steak', 'Bundle of Fireworks', 'Bustling Fungus',
        'Cautious Slug', 'Crowbar', 'Energy Drink', 'Focus Crystal', 'Gasoline', 'Gasoline', "Lens-Maker's Glasses",
        'Medkit', 'Monster Tooth', "Paul's Goat Hoof", 'Personal Shield Generator', 'Repulsion Armor Plate', 'Rusted Key',
        "Soldier's Syringe", 'Sticky Bomb', 'Stun Grenade', 'Topaz Brooch', 'Tougher Times', 'Tri-Tip Dagger', 'Warbanner'
        ]
        
        uncommons = ['AtG Missile Mk. 1', 'Bandolier', "Berzerker's Pauldron", 'Chronobauble', 'Death Mark', 'Fuel Cell',
        "Ghor's Tomb", "Harvester's Scythe", 'Hopoo Feather', 'Infusion', "Kjaro's Band", 'Leeching Seed', 'Lepton Daisy',
        'Old Guillotine', 'Old War Stealthkit', 'Predatory Instincts', 'Razorwire', 'Red Whip', 'Rose Buckler', "Runald's Band",
        'Squid Polyp', 'Ukulele', 'War Horn', 'Wax Quail', "Will-o'-the-wisp"
        ]
        
        legendary = ['57 Leaf Clover', 'Aegis', 'Alien Head', 'Brainstalks', 'Brilliant Behemoth',
        'Ceremonial Dagger', "Dio's Best Friend", 'Frost Relic', 'H3Ad-5T v2', 'Happiest Mask',
        'Hardlight Afterburner', 'Interstellar Desk Plant', "N'kuhana's Opinion", 'Resonance Disk',
        'Sentient Meat Hook', 'Shattering Justice', 'Soulbound Catalyst', 'Unstable Tesla Coil',
        'Wake of Vultures'
        ]
                
        id = ctx.message.author.id
        rarity = randint(0, 100)
        if  0 <= rarity <= 79:
            item = choice(commons)
            pass
        
        elif 79 < rarity <= 99:
            item = choice(uncommons)
        
        else:
            item = choice(legendary)
        
        await ctx.send(F'You recieved {item}!')

        with open('ror2_storage.json') as file:
            player_storage = json.load(file)
        
        if str(id) in player_storage:
            player_storage[str(id)] += item + '\n'
            
        else:
            player_storage[str(id)] = item + '\n'
            
            
        with open('ror2_storage.json', 'w') as add_item_file:
            json.dump(player_storage, add_item_file)
            
            print(F'Saved {item} to member {ctx.message.author} storage')
    
    
    @commands.command(name = 'storage')
    async def showStoredItems(self, ctx: commands.Context):
        id = ctx.message.author.id
        
        with open('ror2_storage.json', 'r') as read_items:
            player_storage = json.load(read_items)
            
        read_items = player_storage[str(id)]
        item_list = read_items.split('\n')
        
        show_items = ''
        for item in item_list:
            if item_list.count(item) > 1:
                show_items += str(item_list.count(item)) + item + '\n'
                continue
            
            show_items += (item + '\n')

        embed = Embed(title = (F"{ctx.message.author}'s items:"), description = show_items)
        await ctx.send(embed = embed)
        
        
def setup(bot: commands.Bot):
    bot.add_cog(RandomStuff(bot))