from flask import Flask, render_template, request, redirect, flash, session,url_for
from backend.login import  LogIn
from dbever.ler_dados import *
from backend.registro_pessoa import Registro_Pessoa
from backend.usuario_comum import Usuario
from flask_session import Session
from dbever.posts_all import *
from flask import Flask, render_template, request, redirect, flash, session,url_for
from backend.login import LogIn
from backend.registro_pessoa import Registro_Pessoa
from backend.usuario_comum import Usuario 
from backend.user_pesquisa_dados import Usuario_pesquisa_dados
from backend.user_salva_dados import Usuario_salva_dados
from flask_session import Session
from dbever.posts_all import PostsAll
from dbever.ler_dados import Ler_dados

