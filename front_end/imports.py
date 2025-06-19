
from flask import Flask, render_template, request, redirect, flash, session,url_for
from backend.login import LogIn
from backend.registro_pessoa import Registro_Pessoa
from backend.usuario_comum import Usuario_Comum 
from flask_session import Session
from dbever.posts_all import Todos_Posts
from dbever.ler_dados import Ler_dados

