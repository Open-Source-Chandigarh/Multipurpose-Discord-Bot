import peewee                     # Used to work on a database
from database import economy_account_db

class Account(peewee.Model):             # Inherits from peewee model i.e. account will be represented as a single table
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    cash : int = peewee.IntegerField()
    bank : int = peewee.IntegerField()
    daily_days : int = peewee.IntegerField()
    
    
    class Meta:
        database = economy_account_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            account = Account.get(Account.user_id == member.id, Account.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            account = Account.create(user_id=member.id, guild_id=member.guild.id, cash=100, bank=100, daily_days = 1)
        return account
