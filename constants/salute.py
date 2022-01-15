from random import choice

async def RockandStone():
    voicelines = ['Rock on!', 'Rock and Stone... Yeeahhh!', 'Rock and Stone forever!',
                  'ROCK...AND...STONE!', 'Rock and Stone!', 'For Rock and Stone!', 'We are unbreakable!',
                  'Rock and Roll!', "That's it lads! Rock and Stone!", 'Rock and Roll and Stone!',
                  'Like that! Rock and Stone!', 'Yeaahhh! Rock and Stone!', 'None can stand before us!',
                  'Rock solid!', 'Come on guys! Rock and Stone!', "If you don't Rock and Stone, you ain't comin' home!",
                  'We fight for Rock and Stone!', 'We rock!', 'Rock and Stone everyone!', 'Rock and Stone in the heart!', 
                  'Did I hear a Rock and Stone?'
                  
                  ]
    
    rock_and_stone = choice(voicelines)
    
    return rock_and_stone