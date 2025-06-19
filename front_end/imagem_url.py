import os
from flask import Flask, request, render_template, url_for, redirect, session
from werkzeug.utils import secure_filename
import uuid
# import mysql.connector # Se você usa mysql.connector diretamente

# 1. Inicialize o aplicativo Flask AQUI
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui' # NECESSÁRIO para sessões

# 2. Defina as configurações globais e variáveis AQUI
# Configuração da pasta de uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Lista de extensões de arquivos permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# 3. Defina a função auxiliar 'allowed_file' AQUI (antes de ser usada)
def allowed_file(filename):
    """Verifica se a extensão do arquivo é permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 4. AGORA você pode definir get_uploaded_image_url()
def get_uploaded_image_url():
    """
    Processa o upload de um arquivo e retorna a URL relativa da imagem
    para ser salva no banco de dados.
    Retorna None se nenhum arquivo válido for enviado ou se houver erro no upload.
    """
    file = request.files.get('file')

    image_url_to_save = None

    if file and file.filename != '' and allowed_file(file.filename):
        filename_original = secure_filename(file.filename)
        file_extension = filename_original.rsplit('.', 1)[1].lower()
        unique_filename = str(uuid.uuid4()) + '.' + file_extension
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename) # app.config e UPLOAD_FOLDER agora estão definidos

        try:
            file.save(filepath)
            image_url_to_save = url_for('static', filename='uploads/' + unique_filename) # app e url_for agora estão definidos
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            image_url_to_save = None

    return image_url_to_save

# ... e o resto do seu código, como as rotas, classes de banco de dados, etc.
# Tudo que usa 'app', 'ALLOWED_EXTENSIONS' ou 'allowed_file' deve vir DEPOIS das definições acima.