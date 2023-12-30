import peewee

economy_account_db = peewee.SqliteDatabase('economy.db')
stats_db = peewee.SqliteDatabase('Player_stats.db')
server_rank_db = peewee.SqliteDatabase('Server_rank.db')
warn_system_db = peewee.SqliteDatabase('warn_system.db')
items_db = peewee.SqliteDatabase('Items.db')