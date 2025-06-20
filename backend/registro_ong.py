
from .registro import *
class EmailJaCadastradoError(Exception):

    pass

class Registro_Ong(Registro):
    def __init__(self, cnpj:str, email:str, senha:str,):
        super().__init__(email,senha)
        self.cnpj = cnpj

        _senha_alterada= self.password_hash(self._senha)
        if Ler_dados.ler_email(self.email) == True:
           raise EmailJaCadastradoError("Este e-mail já está cadastrado.")
           
        Salvamento_Dados.salvar_dados_ong(self,self.cnpj,self.email,_senha_alterada) 

   