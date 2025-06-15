
import pymysql
import dotenv
import os
from .ler_dados import Ler_dados
from .dados import Dados

class Salvamento_Dados(Ler_dados,Dados):

    def salvar_dados(self,nome,email,hash):
            connection = Dados.chama_arquivo()
            with connection.cursor() as cursor:
                  try:
                        sql = 'INSERT INTO REGISTRO (nome, email, pass_hash) VALUES (%s, %s, %s)' # o sql guarda quais colunas eu quero adicionar  #%s funciona como em c
                        cursor.execute(sql, (nome,email,hash))# executa o processo nas colunas que o sql guardou 
                        connection.commit()
                        return True
                  except:
                       print('emaiil ja cadastrado')
                       return False

    
    def salvar_dados_ong(self,cnpj,email,hash):
            connection = Dados.chama_arquivo()
            with connection.cursor() as cursor:
              try:
                sql = 'INSERT INTO REGISTRO (cnpj, email, pass_hash) VALUES (%s, %s, %s)' # o sql guarda quais colunas eu quero adicionar  #%s funciona como em c
                cursor.execute(sql, (cnpj,email,hash))# executa o processo nas colunas que o sql guardou 
                connection.commit()
                return True
              except: 
                   print('emaiil ja cadastrado')
                   return False
    
    
    def salvar_formulario_achados(email,**kwargs):
        usuario_id=Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()
        #id = Ler_dados.pega_id(email) 
        with connection.cursor() as cursor:
    # Corrigindo a consulta SQL
          kwargs['id_usuario'] = usuario_id
          #print(kwargs)
          sql = '''
            INSERT INTO animais_achados
            (id_usuario, tipo_animal, raca, bairro, cidade, rua, horas, infos) 
            VALUES (%(id_usuario)s, %(tipo_animal)s, %(raca)s, %(bairro)s, 
                    %(cidade)s, %(rua)s, %(horas)s, %(infos)s)
        '''
          #print(kwargs)
          cursor.execute(sql, kwargs)
          connection.commit()
          # print("Linhas afetadas:", cursor.rowcount)
          #print('comite realizado')
        
    def salvar_formulario_perdidos(email,**kwargs):
        usuario_id=Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()
            #id = Ler_dados.pega_id(email) 
        with connection.cursor() as cursor:

            kwargs['usuario_id'] = usuario_id
            #print(kwargs)
            sql = '''
                INSERT INTO animais_perdidos
                (usuario_id, tipo_animal, raca, bairro, cidade, rua, horas, infos,nome) 
                VALUES (%(usuario_id)s,%(nome)s, %(tipo_animal)s, %(raca)s, %(bairro)s, 
                        %(cidade)s, %(rua)s, %(horas)s, %(infos)s)
            '''
            #print(kwargs)
            cursor.execute(sql, kwargs)
            connection.commit()
            # print("Linhas afetadas:", cursor.rowcount)
            #print('comite realizado')
#Salva = Salvamento_Dados()
#Salva.salvar_dados('pedro','teste@testetesteadsada','123456')