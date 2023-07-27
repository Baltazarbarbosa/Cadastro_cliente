from sqlalchemy import create_engine

class Postgres:
  connected = False
  def __init__(self,
               host,
               port,
               database,
               user,
               password) -> None:
    self.host = host
    self.port = port
    self.database = database
    self.user = user
    self.password = password

  def connect(self):
    url = "postgresql://{}:{}@{}:{}/{}".format(self.user, 
                                               self.password, 
                                               self.host, 
                                               self.port, 
                                               self.database)
    engine = create_engine(url)
    self.conn = engine.connect()
    self.connected = True

  def disconnect(self):
    if self.connected:
      self.conn.close()
      self.connected = False

  def isConnected(self):
    return self.connected

  def getConnection(self):
    return self.conn