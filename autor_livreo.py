from dataclasses import dataclass 
import os
os.system("Cls")

lista_autores = ("giosepicadura, melbilaw, teukunavara").upper()

@dataclass
class autor:
    nome: str
    biografia: str

@dataclass
class livro:
    titulo: str
    ano: int
    Autor: autor