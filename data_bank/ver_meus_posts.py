from data_bank.dados import Dados

class Meus_Posts(Dados):                
    def meus_posts_usuario_achados(id_usuario):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = (
    "SELECT tipo_animal, bairro, raca, rua, infos, horas, cidade,imagem_url AS detalhe FROM animais_achados WHERE id_usuario = %s "

)
            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchall() 
            return resultado
                

    def meus_posts_usuario_perdidos(id_usuario):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = (
    "SELECT nome, bairro, rua, cidade, horas, tipo_animal, infos, raca ,imagem_url AS detalhe FROM animais_perdidos WHERE usuario_id  = %s "

)
            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchall()  
          
            return resultado
