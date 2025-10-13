from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario

engine = create_engine("sqlite:///meubanco.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome="Victor", email="victor@exemplo.com")
session.add(novo_usuario)
session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

session.close()