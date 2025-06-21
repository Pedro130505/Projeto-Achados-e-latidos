from backend.registro_pessoa import Registro_Pessoa
from data_bank.ler_dados import Ler_dados 


class LogIn:
    erros= 0 
 
    def __init__(self,email:str,senha:str):
      
        self.email=email
        self.senha=senha
    
    def testa_email(self):
        if Ler_dados.ler_email(self.email) is True:
           return True
        else: return False
    def testa_senha(self):
        if Ler_dados.ler_senha(self.senha) is True:
               return True 
                # retorna()
        else:
                    return False 
            
    

    
    def contador_erro_senha():
            global erros
            erros += 1
            print('Senha incorreta!')
            if erros >= 3:
                return False
    

# Início do sistema