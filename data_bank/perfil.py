from data_bank.dados import Dados

class Perfil(Dados):                
    def dados_perfil(self,id_usuario):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = (
    "SELECT nome, email FROM registro WHERE id = %s "

)
            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchall()  
            print(resultado)
            return resultado 
               