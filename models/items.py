import peewee
from database import items_db



class Items(peewee.Model):
    
    # * Only craftable/obtainable from chest
    
        
    
    # * Common tier
    
    bronze_coin: int = peewee.IntegerField()
    junk : int = peewee.IntegerField()
    red_uno : int = peewee.IntegerField()
    blue_uno : int = peewee.IntegerField()
    green_uno : int = peewee.IntegerField()
    yellow_uno : int = peewee.IntegerField()
    adhesive : int = peewee.IntegerField()
    wood : int = peewee.IntegerField()
    bronze_chest : int = peewee.IntegerField()
    
    # * Uncommon tier
    
    silver_coin : int = peewee.IntegerField()
    refining_crystals : int = peewee.IntegerField()
    draw_two_uno : int = peewee.IntegerField()
    reverse_card_uno : int = peewee.IntegerField()
    skip_card_uno : int = peewee.IntegerField()
    gargoyle_essence : int = peewee.IntegerField()
    gargoyle_bones : int = peewee.IntegerField()
    gargoyle_skin : int = peewee.IntegerField()
    gargoyle_fangs : int = peewee.IntegerField()
    goblin_essence : int = peewee.IntegerField()
    goblin_bones : int = peewee.IntegerField()
    iron_ingots : int = peewee.IntegerField()
    rope : int = peewee.IntegerField()
    
    # * Rare tier 
    
    Adventure_map : int = peewee.IntegerField()
    Gold_coin : int = peewee.IntegerField()
    shuffle_card_uno : int = peewee.IntegerField()
    fortress_chest : int = peewee.IntegerField()
    flint : int = peewee.IntegerField()

    
       
       
    class Meta:
        database = items_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            item = Items.get(Items.user_id == member.id, Items.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            item = Items.create(user_id=member.id, guild_id=member.guild.id, hp=100, defense_points=10, damage = 10, crit_rate = 0, crit_dmg = 10, mana = 10)
        return item
