#colocar todas as funções que salvam as coisas
from backend.usuario_comum import Usuario
from dbever.salvadados import *

class Usuario_salva_dados():
    def __init__(self, email ):
        self.email = email 

    def salva_achados(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_achados(email,**kwargs)
      #if=2
    def salva_perdidos(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_perdidos(email,**kwargs)  