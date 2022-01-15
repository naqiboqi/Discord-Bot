from random import choice

async def chooseGame():

    games_list = ['Deep Rock Galactic', 'Control: Ultimate Edition', 'Half Life 3',
    'Portal Reloaded', 'Portal 2', 'Team Fortress 2', 'Risk of Rain 2', 'Hitman 2', 'Space Rig',
    'Shadow of the Tomb Raider', 'Halo Infinite', 'Forza Horizon 5', 'Borderlands 2', 'Borderlands: The Pre-Sequel',
    'Dota 2', 'Europa Universalis IV', 'Mini Motorways', 'Just Cause 3', 'Ace Attorney: Trilogy', 'Resident Evil 2', 'Dishonored',
    'Dishonored 2', 'Metro Exodus', 'Among Us', 'Blender', 'Wolfenstein: The New Colossus', 'TESV: Skyrim', 'Doom Eternal', 'Subnautica',
    'Subnautica: Below Zero', 'Red Dead Redeption 2', 'Grand Theft Auto Five', 'Bioshock: Infinite', 'Kerbal Space Program',
    'Cyberpunk 2077', 'Sea of Thieves', 'Crusader Kings III'
    
    ]

    game_status = choice(games_list) + ' | !help'
    
    return game_status