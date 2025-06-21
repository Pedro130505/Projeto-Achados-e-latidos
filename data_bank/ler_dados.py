
import pymysql
import dotenv
import os
import bcrypt
from .dados import Dados

class Ler_dados(Dados):

    def pega_id(email:str):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = "SELECT id FROM REGISTRO WHERE email = %s"
            cursor.execute(sql, (email,))
            resultado = cursor.fetchone() 
            somente_id = resultado[0]
            return somente_id
        

  
        
    def ler_email(email:str):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
                    dados = ''
                    sql = 'SELECT email FROM REGISTRO '   
                    cursor.execute(sql)
                    dados = cursor.fetchall()
                    for emails in dados:
                        for email_fora_tupla in emails: 
                            if email == email_fora_tupla:
            
                                return True
                                break
                    else:
                        print('n ta na base')
                        return False
    def ler_senha(senha):
        senha_hash=senha.encode('utf-8')
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
                    dados = ''
                    sql = 'SELECT pass_hash FROM REGISTRO '  
                    cursor.execute(sql) 
                    dados = cursor.fetchall()
                    for senhas in dados:
                        print(senhas)
                        for senha_fora_tupla in senhas: 
                            senha_fora_tupla = senha_fora_tupla.encode('utf-8') 
                            if bcrypt.checkpw(senha_hash, senha_fora_tupla):
                                
                                return True            
                    else:
            
                        return False
