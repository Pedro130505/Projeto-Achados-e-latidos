from .dados import Dados


class Filtros(Dados):  
    def filtro_achados(coluna_escolhida,filtro_escolhido):   
        connection = Dados.chama_arquivo()
    

        colunas_validas = ['tipo_animal', 'bairro', 'raca', 'rua', 'infos', 'horas', 'cidade']
        coluna = coluna_escolhida
        if coluna_escolhida not in colunas_validas:
            print("Coluna inválida. Tente novamente.")
            return []
        
        filtro = filtro_escolhido
        
        with connection.cursor() as cursor: 
            query = f"""
SELECT tipo_animal, bairro, raca, rua, infos, horas, cidade AS detalhe
FROM animais_achados
WHERE {coluna_escolhida} = %s
"""
            cursor.execute(query, (filtro_escolhido,))
            resultado = cursor.fetchall()
        print(resultado)
        return resultado
    
    def filtro_perdidos(coluna_escolhida,filtro_escolhido):   
                connection = Dados.chama_arquivo()
            

                colunas_validas = ['tipo_animal', 'bairro', 'raca', 'rua', 'infos', 'horas', 'cidade']
                coluna = coluna_escolhida
                if coluna_escolhida not in colunas_validas:
                    print("Coluna inválida. Tente novamente.")
                    return []
                
                filtro = filtro_escolhido
                
                with connection.cursor() as cursor: 
                    query = f"""
        SELECT nome,tipo_animal, bairro, raca, rua, infos, horas, cidade AS detalhe
        FROM animais_perdidos
        WHERE {coluna_escolhida} = %s
        """
                    cursor.execute(query, (filtro_escolhido,))
                    resultado = cursor.fetchall()
                print(resultado)
                return resultado
