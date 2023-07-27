from . import postgresql
###

class PostgresManager:
  def getInstance():
    try:
      host = "postgres"
      port = 5432
      database = "postgres"
      user = "postgres"
      password = "postgres"
      
      return postgresql.Postgres(host=host,
                                 port=port,
                                 database=database,
                                 user=user,
                                 password=password)
    except Exception as error:
      raise error
