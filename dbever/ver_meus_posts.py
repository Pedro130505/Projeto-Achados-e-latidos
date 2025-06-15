from dbever.dados import Dados


class Ver_meus_posts(Dados):                
    def posts_usuario_achados(id_usuario):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = (
    "SELECT tipo_animal, bairro, raca, rua, infos, horas, cidade AS detalhe FROM animais_achados WHERE id_usuario = %s "

)
            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchall()  # fetchall para pegar todos os registros
            return resultado
                

    def posts_usuario_perdidos(id_usuario):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = (
    "SELECT nome,tipo_animal, bairro, raca, rua, infos, horas, cidade AS detalhe FROM animais_perdidos WHERE usuario_id = %s "

)
            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchall()  # fetchall para pegar todos os registros
            #for posts in resultado:
                #return posts
            return resultado
