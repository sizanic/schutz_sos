from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename  
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions  

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/formulaire_ranger/')
def FormulaireRanger():
    # Afficher la page HTML
    return render_template('form_ranger.html')

@app.route('/ajouter_composant/, methods=['POST']') 
def RangerComposant():

    allee_id = request.form['allee']
    empl_id = request.form['emplacement']
    ref_id = request.form['reference']

    conn = sqlite3.connect('schutz.db')
    cursor = conn.cursor()
    cursor.execute('insert into inventaire (REF) values(?, ?, ?)', (allee_id, empl_id, ref_id))
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return redirect('/formulaire_ranger/')  # Rediriger vers la page d'accueil après l'enregistrement

@app.route('/formulaire_vider/')
def FormulaireVider():
    # Afficher la page HTML pour vider un emplacement
    return render_template('form_vider.html')
	
@app.route('/vider_emplacement/, methods=['POST']')
def ViderEmplacement():

    allee_id = request.form['allee']
    empl_id = request.form['emplacement']
    
   conn = sqlite3.connect('schutz.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM emplacements WHERE allee_id = 'A' AND emplacement_id = 103, (allee_id, empl_id))
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return redirect('/formulaire_vider/')  # Rediriger vers la page d'accueil après


@app.route('/recherche/')
def ReadBDD():
    conn = sqlite3.connect('schutz.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ref,date FROM inventaire;')
    data = cursor.fetchall()
    conn.close()
    return render_template('/formulaire_ranger/')

@app.route('/livres/')
def ReadBDD2():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)






