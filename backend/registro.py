from data_bank.salvadados import Salvamento_Dados
from data_bank.ler_dados import Ler_dados

import bcrypt

class EmailJaCadastradoError(Exception):
  
    pass

class Registro:
    def __init__(self, senha:str, email:str):
      
        self._senha = senha
        self.email = email
      #jogar infos no banco de daDOS 
        # fazer umj if email ja esta na base de dados 
        _senha_alterada= self.password_hash(self._senha)


    def password_hash(self,senha):

        senha_bytes = senha.encode('utf-8')

        salt = bcrypt.gensalt()  # Gera um salt aleatório e seguro

        # Hashing Password
        hashed = bcrypt.hashpw(password=senha_bytes, salt=salt)  # Gera o hash da senha usando o salt
        return hashed 
        # Hashed Password
        #print(f"Hashed Password: {hashed.decode('utf-8')}")
