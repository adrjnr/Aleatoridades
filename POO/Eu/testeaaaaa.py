from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session 

class Banco:
    def __init__(self, url):
        self.__engine = create_engine(url)

    def get_engine(self):
        return self.__engine
    
class Base(DeclarativeBase):
    pass

class Produto(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    preco: Mapped[float] = mapped_column()
    estoque: Mapped[float] = mapped_column()

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.set_preco(preco)
        self.set_estoque(estoque)
        
    def set_preco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.preco = preco

    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self.estoque = estoque

if __name__ == "__main__":
    bd = Banco('sqlite:///usuarios.db')
    Base.metadata.create_all(bd.get_engine())

    with Session(bd.get_engine()) as session:
        while True:
            print('1-adiciona produto\n2-atualiza preco\n3-atualiza estoque\n4-lista produtos\n0-sair')
            op = int(input('Escolha um: '))

            match op:
                case 1:
                    nome = input('nome: ')
                    preco = float(input('preco: '))
                    estoque = float(input('estoque: '))
                    produto = Produto(nome, preco, estoque)
                    session.add(produto)
                    session.commit()
                
                case 2:
                    id = int(input('ID do produto a atualizar: '))
                    produto = session.query(Produto).filter_by(id=id).first()
                    if produto:
                        preco = float(input('novo preco: '))
                        produto.set_preco(preco)
                        session.commit()
                case 3:
                    id = int(input('ID do produto a atualizar: '))
                    produto = session.query(Produto).filter_by(id=id).first()
                    if produto:
                        estoque = float(input('novo estoque: '))
                        produto.set_estoque(estoque)
                        session.commit()
                case 4:
                    produtos = session.query(Produto).all()
                    for c in produtos:
                        print(f'{c.id} | {c.nome} | {c.preco} | {c.estoque}')
                case 0:
                    break