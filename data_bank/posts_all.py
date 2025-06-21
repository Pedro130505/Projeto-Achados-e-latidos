from data_bank.dados import Dados

class Todos_Posts(Dados):

    @staticmethod
    def posts_usuarios_achados():
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = "SELECT tipo_animal, bairro, raca, rua, infos, horas, cidade,imagem_url AS detalhe FROM animais_achados"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            
            return resultado  

    @staticmethod
    def posts_usuarios_perdidos():
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = "SELECT nome, tipo_animal, bairro, raca, rua, infos, horas, cidade,imagem_url AS detalhe FROM animais_perdidos"
            cursor.execute(sql)
            resultado = cursor.fetchall()
        
            return resultado  
