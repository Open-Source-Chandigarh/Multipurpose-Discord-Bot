import peewee
from database import stats_db


class Stats(peewee.Model):
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    hp : int = peewee.IntegerField()
    defense_points : int = peewee.IntegerField()
    damage : int = peewee.IntegerField()
    crit_rate : int = peewee.IntegerField()
    crit_dmg : int = peewee.IntegerField()
    mana : int = peewee.IntegerField()
       
       
    class Meta:
        database = stats_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            stats = Stats.get(Stats.user_id == member.id, Stats.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            stats = Stats.create(user_id=member.id, guild_id=member.guild.id, hp=100, defense_points=10, damage = 10, crit_rate = 0, crit_dmg = 10, mana = 10)
        return stats
