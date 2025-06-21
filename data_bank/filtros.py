from .dados import Dados



class Filtros(Dados):  
    def filtro_achados(self, coluna_escolhida, filtro_escolhido):
        connection = Dados.chama_arquivo()
        colunas_validas = ['tipo_animal', 'bairro', 'raca', 'rua', 'infos', 'horas', 'cidade']

        if coluna_escolhida not in colunas_validas:
            print("Coluna inválida. Tente novamente.")
            return []

        query = f"""
        SELECT tipo_animal, bairro, raca, rua, infos, horas, cidade,imagem_url AS detalhe
        FROM animais_achados
        WHERE TRIM(LOWER({coluna_escolhida})) = TRIM(LOWER(%s))
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (filtro_escolhido.strip().lower(),))
                resultado = cursor.fetchall()
                print("Resultado (Achados):", resultado)
                return resultado
        except Exception as e:
            print("Erro ao executar filtro_achados:", e)
            return []

    def filtro_perdidos(self, coluna_escolhida, filtro_escolhido):
        connection = Dados.chama_arquivo()
        colunas_validas = ['tipo_animal', 'bairro', 'raca', 'rua', 'infos', 'horas', 'cidade']

        if coluna_escolhida not in colunas_validas:
            print("Coluna inválida. Tente novamente.")
            return []

        query = f"""
        SELECT nome, tipo_animal, bairro, raca, rua, infos, horas, cidade,imagem_url AS detalhe
        FROM animais_perdidos
        WHERE TRIM(LOWER({coluna_escolhida})) = TRIM(LOWER(%s))
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (filtro_escolhido.strip().lower(),))
                resultado = cursor.fetchall()
                print("Resultado (Perdidos):", resultado)
                return resultado
        except Exception as e:
            print("Erro ao executar filtro_perdidos:", e)
            return []

        
