from config import CONN, CURSOR

class Song:
    def __init__(self,name,album):
        self.name = name
        self.album = album
        
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        
    def save(self):
        sql = """ 
            INSERT INTO songs (name, album)
            VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

blinding_lights = Song("Blinding Lights","After Hours")
blinding_lights.save()

despacito = Song("Despacito","Vida")
despacito.save()

song = Song.create("Hello", "25")
song.name
song.album
