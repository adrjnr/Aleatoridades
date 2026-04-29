class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        
    def __str__(self):
        return f'Nome: {self.nome}\nTipo: {self.tipo}'
    
    def ataque(self):
        return f'Brasa'
    
    
if __name__ == "__main__":
    pokemon1 = Pokemon('Charmander', 'fogo')
    
    print(pokemon1.nome, f"usou", pokemon1.ataque(), f"do tipo", pokemon1.tipo)
    print("O ataque foi super efetivo!") 
    