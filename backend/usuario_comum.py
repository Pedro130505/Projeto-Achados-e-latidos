from backend.usuario_abstrato import *

class Usuario_Comum(Usuario):  
#deixar apenas as que exibem dados 
    def __init__(self, email):
          self.email=email
 
    def adm(self):
         False


    def perfil(self):
          return Perfil.dados_perfil(self,self.get_id())
      
 
    def pesquisa_meus_posts_animais_achados(self):
            return Meus_Posts.meus_posts_usuario_achados(self.get_id())
            
    def pesquisa_meus_posts_animais_perdidos(self):    
           return Meus_Posts.meus_posts_usuario_perdidos(self.get_id())
         
    
      #if =1
    def salva_achados(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_achados(email,**kwargs)
      #if=2
    def salva_perdidos(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_perdidos(email,**kwargs)  
      # if =3 
    def pesquisa_achados(self):
         return Todos_Posts.posts_usuarios_achados()
          
    def pesquisa_perdidos(self):
         return Todos_Posts.posts_usuarios_perdidos()
      #filtro
    def posts_achados_filtrado(self,coluna,valor):
         return Filtros.filtro_achados(self,coluna,valor)

    def posts_perdidos_filtrado(self,coluna,valor):
          return Filtros.filtro_perdidos(self,coluna,valor) 
    


#a =Usuario('teste4@')
#a.perfil()


