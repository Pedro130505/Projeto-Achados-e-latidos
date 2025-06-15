from backend.registro_pessoa import Registro_Pessoa
from dbever.ler_dados import Ler_dados 


def retorna():
    return True 
def retorna2():
    return False

class LogIn:
    erros= 0 
 
    def __init__(self,email:str,senha:str):
      
        self.email=email
        if Ler_dados.ler_email(self.email) is True:
          
            self.senha=senha
            if Ler_dados.ler_senha(self.senha) is True:
                print("Login bem-sucedido!")
               # retorna()

            else:
                self.contador_erro_senha()
                #self.__init__()
                print('Senha errada')
                #retorna2()
        else:
            print('Senha errada')
            #retorna2()
           #self.cadastrar()
           # self.__init__()  # Tenta logar novamente após cadastro
      
    
    def contador_erro_senha():
            global erros
            erros += 1
            print('Senha incorreta!')
            if erros >= 3:
                print('Sua conta foi bloqueada momentaneamente.')
    

# Início do sistema