import peewee                     # Used to work on a database
from database import warn_system_db

class Warn_system(peewee.Model):             # Inherits from peewee model i.e. account will be represented as a single table
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    warns: int = peewee.IntegerField()
    
    
    class Meta:
        database = warn_system_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            account = Warn_system.get(Warn_system.user_id == member.id, Warn_system.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            account = Warn_system.create(user_id=member.id, guild_id=member.guild.id, warns = 0)
        return account
