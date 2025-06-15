
from dbever.ver_meus_posts import*
from dbever.posts_all import *
from backend.usuario_comum import Usuario

class Usuario_pesquisa_dados():
    def __init__(self, email):
        super().__init__(email)

    def pesquisa_meus_posts_animais_achados(self):
            return Ver_meus_posts.posts_usuario_achados(self.get_id())
            
    def pesquisa_meus_posts_animais_perdidos(self):    
           return Ver_meus_posts.posts_usuario_perdidos(self.get_id())
           
    

    def pesquisa_achados(self):
         return PostsAll.posts_usuarios_achados()
          
    def pesquisa_perdidos(self):
         return  PostsAll.posts_usuarios_perdidos()