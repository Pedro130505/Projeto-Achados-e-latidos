
from backend.imports_usuario import *

class Usuario(Registro_Pessoa): 
    def __init__(self, email):
          self.email=email
      


    @abstractmethod
    def adm():
          pass

    def get_id(self,):
          id = Ler_dados.pega_id(self.email)
          return id
    


