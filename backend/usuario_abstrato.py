
from backend.imports_usuario import *

class Usuario_abs(Registro_Pessoa): 
    def __init__(self, email):
          self.email=email
        # Registro.__init__(email)


    @abstractmethod
    def adm():
          pass

    def get_id(self,):
          id = Ler_dados.pega_id(self.email)
          return id
    


