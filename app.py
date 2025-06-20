from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_session import Session
from dbever.ler_dados import Ler_dados
from backend.login import LogIn
from backend.usuario_comum import Usuario_Comum
from backend.registro_ong import Registro_Ong
from backend.notificacao_gmail import Notificacao_Email
from backend.registro_pessoa import Registro_Pessoa
from front_end.imagem_url import *

def teste():
    app = Flask(__name__)
    app.secret_key = 'seu_valor_aqui'
    app.config['SESSION_TYPE'] = 'filesystem'

    Session(app)

  
    @app.route('/registro_ong', methods=['GET'])
    def registro_ong_chama():
        return render_template('registro_ong.html')


    @app.route('/registro_ong', methods=['POST'])
    def registro_ong():
        email = request.form['email']
        senha = request.form['senha']
        cnpj = request.form['cnpj']
        try:
            novo_usuario = Registro_Ong(cnpj, email, senha)
            notificação = Notificacao_Email(email)
            notificação.manda_notificacao()
            return redirect(url_for('index'))
        except Exception as e :
            print(f"Erro ao cadastrar: {e}")  # mostra no terminal
            flash(str(e), 'erro')  
            return redirect(url_for('registro_ong_chama', message="Email já cadastrado. Tente novamente.", type="error"))


  
    @app.route('/registro', methods=['GET'])
    def registro_chama():
        return render_template('registro.html')


    @app.route('/registro', methods=['POST'])
    def registro():
        email = request.form['email']
        senha = request.form['senha']
        nome = request.form['nome']
        try:
            novo_usuario = Registro_Pessoa(nome, email, senha)
            notificação = Notificacao_Email(email)
            notificação.manda_notificacao()
            return redirect(url_for('index'))
        except Exception as e:
                #print(f"Erro ao cadastrar: {e}")  # mostra no terminal
                #flash(str(e), 'erro')    
                return redirect(url_for('registro_chama', message="Email já cadastrado. Tente novamente.", type="error"))



    @app.route('/')
    def index():
        return render_template('login.html')


    @app.route('/login', methods=['POST'])
    def login():
        email = request.form['email']
        senha = request.form['senha']
         
        # In a real application, you would typically instantiate LogIn and use its methods
        # For a basic check, assuming Ler_dados handles the actual verification
        login = LogIn(email,senha)
        if login.testa_email() is False:
            return render_template('login.html', mensagem="Email não cadastrado. Tente novamente.")
        if login.testa_senha() is False: 
             return render_template('login.html', mensagem="Senha Incorreta.")
        #if login.contador_erro_senha is False:
           # return render_template('login.html', mensagem="Conta bloqueada por 5 minutos.")
        else:
            session['usuario_email'] = email
            return redirect('/main')
        '''
        if Ler_dados.ler_email(email) == False:
            return render_template('login.html', mensagem="Email não cadastrado. Tente novamente.")
        else:
            if Ler_dados.ler_senha(senha):
                session['usuario_email'] = email
                return redirect('/main')
            else:
                 return render_template('login.html', mensagem="Senha Incorreta.")
            #else:
                #return render_template('login.html', mensagem="Senha incorreta. Tente novamente.")
       '''

    # ------------------------ MAIN ------------------------
    @app.route('/main', methods=['GET'])
    def main_chama():
        return render_template('main.html')

    @app.route('/main', methods=['POST'])
    def main():
        print('Ação POST main')
        return redirect('/main')

    # ------------------------ ANIMAIS ------------------------
    @app.route('/animais', methods=['GET'])
    def animais_perdidos():
        return render_template('animais.html')

    @app.route('/animais', methods=['POST'])
    def animais():
        usuario_email = session.get('usuario_email')  
        escolha = request.form['escolha']
        session['escolha'] = escolha

        if escolha == "1":
            return redirect('/registrar_animais_achados')
        elif escolha == "2":
            return redirect('/registrar_animais_perdidos')
        elif escolha == "4":
            return redirect('/pesquisar')
        else:
            return "Escolha inválida", 400

    # ------------------------ FORM ANIMAIS ACHADOS ------------------------
    @app.route('/registrar_animais_achados', methods=['GET'])
    def registrar_animais_achados_form():
        return render_template('registrar_animais_achados.html')

    @app.route('/registrar_animais_achados', methods=['POST'])
    def registrar_animais_achados_salva():
        imagem_url_salva = get_uploaded_image_url()
        usuario_email = session.get('usuario_email')  
        dados = {
            'tipo_animal': request.form['tipo_animal'],
            'raca': request.form['raca'],
            'cidade': request.form['cidade'],
            'bairro': request.form['bairro'],
            'rua': request.form['rua'],
            'horas': request.form['horas'],
            'infos': request.form['infos'],
            'imagem_url':imagem_url_salva ,
        }
        usuario = Usuario_Comum(usuario_email)
        usuario.salva_achados(usuario_email, **dados)
        return redirect('/animais')

    # ------------------------ FORM ANIMAIS PERDIDOS ------------------------
    @app.route('/registrar_animais_perdidos', methods=['GET'])
    def registrar_animais_perdidos_form():
        return render_template('registrar_animais_perdidos.html')

    @app.route('/registrar_animais_perdidos', methods=['POST'])
    def registrar_animais_perdidos_salva():
        imagem_url_salva = get_uploaded_image_url()
        usuario_email = session.get('usuario_email')  
        dados = {
            'nome': request.form['nome'],
            'tipo_animal': request.form['tipo_animal'],
            'raca': request.form['raca'],
            'cidade': request.form['cidade'],
            'bairro': request.form['bairro'],
            'rua': request.form['rua'],
            'horas': request.form['horas'],
            'infos': request.form['infos'],
            'imagem_url':imagem_url_salva
        }
        usuario = Usuario_Comum(usuario_email)
        usuario.salva_perdidos(usuario_email, **dados)
        return redirect('/animais')

    # ------------------------ PESQUISA ------------------------
    
    @app.route('/pesquisar', methods=['GET', 'POST'])
    def pesquisar_animais():
        if request.method == 'POST':
            usar_filtro = request.form.get('usar_filtro')
            if usar_filtro == 'sim':
                usuario_email = session.get('usuario_email')
                usuario = Usuario_Comum(usuario_email)
                coluna = request.form.get('coluna', '')
                valor = request.form.get('valor', '')
                achados = usuario.posts_achados_filtrado(coluna, valor)
                perdidos = usuario.posts_perdidos_filtrado(coluna, valor)
                print(perdidos, achados)
                return render_template('pesquisar.html',
                                    achados=achados,
                                    perdidos=perdidos,
                                    usar_filtro=usar_filtro,
                                    coluna=coluna,
                                    valor=valor)
            else:
                usuario_email = session.get('usuario_email')
                usuario = Usuario_Comum(usuario_email)
                achados = usuario.pesquisa_achados()
                perdidos = usuario.pesquisa_perdidos()
                return render_template('pesquisar.html',
                                    achados=achados,
                                    perdidos=perdidos,
                                    usar_filtro=usar_filtro)
        else:
            # método GET: exibir tudo por padrão
            usuario_email = session.get('usuario_email')
            usuario = Usuario_Comum(usuario_email)
            achados = usuario.pesquisa_achados()
            perdidos = usuario.pesquisa_perdidos()
            return render_template('pesquisar.html',
                                achados=achados,
                                perdidos=perdidos,
                                usar_filtro='nao')
          

    # ------------------------ SOBRE NÓS ------------------------
    @app.route('/sobrenos')
    def sobre_nos():
        return render_template('sobrenos.html')

    # ------------------------ PERFIL ------------------------
    @app.route('/suaconta', methods=['GET', 'POST'])
    def ver_perfil():
        email_sessao = session.get('usuario_email')
        usuario = Usuario_Comum(email_sessao)
        dados_brutos = usuario.perfil()
        nome_usuario = dados_brutos[0][0]
        email_usuario = dados_brutos[0][1]
        achados = usuario.pesquisa_meus_posts_animais_achados()
        perdidos = usuario.pesquisa_meus_posts_animais_perdidos()

        return render_template('suaconta.html', nome=nome_usuario, email=email_usuario,achados=achados,
                                    perdidos=perdidos,)

    return app # <--- ADD THIS LINE HERE!

if __name__ == '__main__':
    app = teste()
    app.run(debug=True)