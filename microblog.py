from flask import Flask 

app = Flask("microblog") #O Flask faz com que sejam relacionadas url e comandos do python 
                         #(toda vez que chegar em determinada url, x comando será executado

@app.route("/") #O arroba no python tem uma sintaxe conhecida como "decorator", a função route faz com que quando se entre na url no app, seja executada a função abaixo 
def index():
    return "Olá mundo"

app.run()