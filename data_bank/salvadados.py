
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
                        sql = 'INSERT INTO REGISTRO (nome, email, pass_hash) VALUES (%s, %s, %s)'
                        cursor.execute(sql, (nome,email,hash))
                        connection.commit()
                        return True
                  except:
                       print('emaiil ja cadastrado')
                       return False

    
    def salvar_dados_ong(self,cnpj,email,hash):
            connection = Dados.chama_arquivo()
            with connection.cursor() as cursor:
              try:
                sql = 'INSERT INTO REGISTRO (cnpj, email, pass_hash) VALUES (%s, %s, %s)' 
                cursor.execute(sql, (cnpj,email,hash))
                connection.commit()
                return True
              except: 
                   print('emaiil ja cadastrado')
                   return False
    
    
    @staticmethod
    def salvar_formulario_achados(email, **kwargs):
        usuario_id = Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()

        campos_para_lower = ['tipo_animal', 'raca', 'bairro', 'cidade', 'rua', 'horas', 'infos']
        for campo in campos_para_lower:
            if campo in kwargs and isinstance(kwargs[campo], str):
                kwargs[campo] = kwargs[campo].strip().lower()

        kwargs['id_usuario'] = usuario_id  

        sql = '''
            INSERT INTO animais_achados
            (id_usuario, tipo_animal, raca, bairro, cidade, rua, horas, infos, imagem_url) 
            VALUES (%(id_usuario)s, %(tipo_animal)s, %(raca)s, %(bairro)s, 
                    %(cidade)s, %(rua)s, %(horas)s, %(infos)s, %(imagem_url)s)
        '''

        with connection.cursor() as cursor:
            cursor.execute(sql, kwargs)
            connection.commit()

    @staticmethod
    def salvar_formulario_perdidos(email, **kwargs):
        usuario_id = Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()

   
        campos_para_lower = ['tipo_animal', 'raca', 'bairro', 'cidade', 'rua', 'horas', 'infos']
        for campo in campos_para_lower:
            if campo in kwargs and isinstance(kwargs[campo], str):
                kwargs[campo] = kwargs[campo].strip().lower()

        kwargs['usuario_id'] = usuario_id  
        sql = '''
            INSERT INTO animais_perdidos
            (nome, bairro, rua, cidade, horas, tipo_animal, infos, raca, usuario_id, imagem_url) 
            VALUES (%(nome)s, %(bairro)s, %(rua)s, %(cidade)s, %(horas)s, 
                    %(tipo_animal)s, %(infos)s, %(raca)s, %(usuario_id)s, %(imagem_url)s)
        '''

        with connection.cursor() as cursor:
            cursor.execute(sql, kwargs)
            connection.commit()