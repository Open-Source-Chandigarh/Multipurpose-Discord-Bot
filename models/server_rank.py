import peewee                     # Used to work on a database
from database import server_rank_db

class server_rank(peewee.Model):             # Inherits from peewee model i.e. account will be represented as a single table
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    Level: int = peewee.IntegerField()
    Experience: int = peewee.IntegerField()
    
    
    class Meta:
        database = server_rank_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            account = server_rank.get(server_rank.user_id == member.id, server_rank.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            account = server_rank.create(user_id=member.id, guild_id=member.guild.id, Level = 0, Experience = 0)
        return account
