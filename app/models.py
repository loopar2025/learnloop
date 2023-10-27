from app import db


class User(db.Model):
  id = db.Column(db.String(), primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  password = db.Column(db.String())

  def __init__(self, id, username, password):
    self.id = id
    self.username = username
    self.password = password


class Artigo(db.Model):
  id = db.Column(db.String(), primary_key=True)
  titulo = db.Column(db.String(128))
  texto = db.Column(db.String(1024))
  autor = db.Column(db.String(64))
  data = db.Column(db.String(64))
  categoria = db.Column(db.String(64))
  tags = db.Column(db.String(64))
  likes = db.Column(db.Integer)

  def __init__(self, titulo, texto, autor, data, categoria, tags, likes):
    self.titulo = titulo
    self.texto = texto
    self.autor = autor
    self.data = data
    self.categoria = categoria
    self.tags = tags
    self.likes = likes


class Material(db.Model):
  id = db.Column(db.String(), primary_key=True)
  nome = db.Column(db.String(255))
  link = db.Column(db.String())
  autor = db.Column(db.String())


class Complementos(db.Model):
  id = db.Column(db.String(), primary_key=True)
  autor = db.Column(db.String())
  text = db.Column(db.String())
  artigo = db.Column(db.String())
