# this is the main app file
from flask import Flask,url_for,render_template, redirect, request,flash, g
import sqlite3
from functions import *


app_info = {
    'db_file':'/home/nenow/1_web_apps/StronaMlodegoProgramisty/data/smp.db'
    #'db_file':'/home/nenow79/1_MyScripts/flask/StronaMlodegoProgramisty/data/smp.db'
    #'db_file':r'C:\Users\pawel\Desktop\1_My_scripts\StronaMlodegoProgramisty\data\smp.db'
}


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')



def get_db():
    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
#################################
@app.route('/informatyka')
def fizyka():
    return render_template('informatyka.html')

@app.route('/fizyka/predkosc',methods=['GET','POST'])
def fizyka_predkosc():
    if request.method == 'GET':
        return render_template('fizyka_predkosc.html')
    else:
        print('-'*20)
        print(request.form)

        droga_unit= 'km'
        if 'droga_unit' in request.form:
            droga_unit = request.form['droga_unit']
        droga='100'
        if 'droga' in request.form:
            droga = request.form['droga']

        czas_unit='h'
        if 'czas_unit' in request.form:
            czas_unit = request.form['czas_unit']
        czas='1'
        if 'czas' in request.form:
            czas = request.form['czas']

        predkosc = oblicz_predkosc(droga,droga_unit,czas,czas_unit)
        return render_template('fizyka_predkosc_results.html',droga_unit=droga_unit,droga=droga,czas_unit=czas_unit,czas=czas,predkosc=predkosc)

@app.route('/tata/procent_alk',methods=['GET','POST'])
def procent_alk():
    if request.method == 'GET':
        return render_template('tata_procent_alk.html')
    else:
        obj_1 = float(request.form['obj_1']) if request.form['obj_1_unit'] == 'l' else float(request.form['obj_1']) / 1000
        obj_2 = float(request.form['obj_2']) if request.form['obj_2_unit'] == 'l' else float(request.form['obj_2']) / 1000
        r = Roztwor_alkoholu(obj_1, request.form['alk_1'], obj_2, request.form['alk_2'],)
        print(r.roztwor())
        return render_template('tata_procent_alk_result.html',r=r)

@app.route('/tata/wino_cukier',methods=['GET','POST'])
def wino_cukier():
    if request.method == 'GET':
        return render_template('tata_wino_cukier.html')
    else:
        print(request.form)
        obj = request.form['obj']
        alk = request.form['alk']
        w = Wino_cukier(obj,alk)
        return render_template('tata_wino_cukier_result.html',w=w)


########################################
@app.route('/kuchnia',methods=['GET','POST'])
def kuchnia():
    db = get_db()

    if request.method == 'POST':
        sql_command = 'insert into przepisy2(name, skladniki, przepis, autor) values(?, ?, ?, ?)'
        nazwa_przepisu = request.form['nazwa_przepisu']
        skladniki_przepisu = request.form['skladniki_przepisu']
        tresc_przepisu = request.form['tresc_przepisu']
        autor_przepisu = request.form['autor_przepisu']
        db.execute(sql_command, [nazwa_przepisu, skladniki_przepisu, tresc_przepisu, autor_przepisu])
        db.commit()

    sql_command = 'select * from przepisy2;'
    cur = db.execute(sql_command)
    przepisy = cur.fetchall()
    return render_template('kuchnia.html',przepisy=przepisy)

@app.route('/kuchnia/nowy_przepis')
def nowy_przepis():
    return render_template('nowy_przepis.html')

@app.route('/kuchnia/admin',methods=['GET','POST'])
def kuchnia_admin():
    db = get_db()
    if request.method == 'POST' and request.form['akcja']=='delete':
        sql_command = 'DELETE FROM przepisy2 WHERE id = ?;'
        db.execute(sql_command, [request.form['id_przepisu']])
        db.commit()
        return redirect(url_for('kuchnia'))
    elif request.method == 'POST' and request.form['akcja']=='edit':
        return redirect(url_for('edytuj_przepis',ID=request.form['id_przepisu']))
    return render_template('kuchnia_admin.html')

@app.route('/kuchnia/edytuj_przepis/<ID>',methods=['GET','POST'])
def edytuj_przepis(ID):
    db = get_db()
    if request.method == 'POST':
        sql_command = 'UPDATE przepisy2 SET name=?, skladniki=?, przepis=?, autor=? where id=?'
        nazwa_przepisu = request.form['nazwa_przepisu']
        skladniki_przepisu = request.form['skladniki_przepisu']
        tresc_przepisu = request.form['tresc_przepisu']
        autor_przepisu = request.form['autor_przepisu']
        db.execute(sql_command, [nazwa_przepisu, skladniki_przepisu, tresc_przepisu, autor_przepisu, ID])
        db.commit()
        return redirect(url_for('kuchnia'))

    sql_command = 'SELECT * FROM przepisy2 WHERE id =?;'
    cur = db.execute(sql_command,[ID])
    przepis = cur.fetchone()

    return render_template('edytuj_przepis.html',przepis=przepis)
