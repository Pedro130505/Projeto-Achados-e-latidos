from backend.usuario_abstrato import *

class Adm(Usuario):
      
    def __init__(self, email:str):
          self.email=email
    def adm():
          True

    def perfil(self):
          return Perfil.dados_perfil(self,self.get_id())
      