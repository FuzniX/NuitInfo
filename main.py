from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

# Page d'accueil du site
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/footer/<page>.html')
def footer(page):
    return render_template(f'footer/{page}.html')

# Gestion de l'erreur 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

############################## NE PAS MODIFIER LE CODE SUIVANT ##############################
if __name__ == '__main__':                                                                  #
    app.run(debug=False, host='0.0.0.0', port=26004)                                        #
#############################################################################################