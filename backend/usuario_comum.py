from backend.usuario_abstrato import *

class Usuario(Usuario_abs):  
#deixar apenas as que exibem dados 
    def __init__(self, email):
          self.email=email
 
    def adm(self):
         False


    def perfil(self):
          return Perfil.dados_perfil(self,self.get_id())
      
 
    def pesquisa_meus_posts_animais_achados(self):
            return Ver_meus_posts.posts_usuario_achados(self.get_id())
            
    def pesquisa_meus_posts_animais_perdidos(self):    
           return Ver_meus_posts.posts_usuario_perdidos(self.get_id())
         
    
      #if =1
    def salva_achados(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_achados(email,**kwargs)
      #if=2
    def salva_perdidos(self,email,**kwargs):
          Salvamento_Dados.salvar_formulario_perdidos(email,**kwargs)  
      # if =3 
    def pesquisa_achados(self):
          PostsAll.posts_usuarios_achados()
          
    def pesquisa_perdidos(self):
          PostsAll.posts_usuarios_perdidos()
 #filtro
    def posts_achados_filtrado(self,coluna,valor):
         return Filtros.filtro_achados(coluna,valor)

    def posts_perdidos_filtrado(self,coluna,valor):
          return Filtros.filtro_perdido(coluna,valor) 
    #def excluir(self): 
                #print(posts_ligados_email[self.email])


#a =Usuario('teste4@')
#a.perfil()



    #FILTROS, RECEBER NOMES DAS COISAS SEMPRE SEM LETRA MAIUSCU
    # FAZER ÁGINA RECEBNDO SUA CONTA EMAIL E USARIO JUNTO COM SEUS POSTS'''

