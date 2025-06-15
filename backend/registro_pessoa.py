
from .registro import *
from dbever.ler_dados import Ler_dados
# Em backend/registro.py (ou um arquivo de exceções como backend/erros.py)

class EmailJaCadastradoError(Exception):
    """Exceção levantada quando um e-mail tentado para registro já existe."""
    pass

class Registro_Pessoa(Registro):
    def __init__(self, nome:str, email:str, senha:str):
        super().__init__(senha,email)
        self.nome=nome

        _senha_alterada= self.password_hash(self._senha)
        if Ler_dados.ler_email(self.email) == True:
            # Se salvar_dados retornar False, levante uma exceção
             raise EmailJaCadastradoError("Este e-mail já está cadastrado.")
        
        Salvamento_Dados.salvar_dados(self,self.nome,self.email,_senha_alterada) 
