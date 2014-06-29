# coding=UTF8
import os 
import xml.etree.ElementTree as ET
from flask import Flask, url_for
app = Flask(__name__)

D = {}
diretorio = __file__.rpartition("/")[0]
diretorioxmls = diretorio+"/static/bios/"
xmls = os.listdir(diretorioxmls)
for xml in xmls:
    raiz = ET.parse(diretorioxmls+xml)
    deps = raiz.findall("./DATA_RECORD")

    for dep in deps:
        cod = dep.find("CODPESSOA").text
        crian = dep.getchildren()
        d = {}
        for c in crian:
            d[c.tag] = c.text
        D[cod] = d
    
print "processados!"

LISTAALFAB = sorted(D.values(), key=lambda dep: dep["TXTNOME"]) 
LISTACRONO = sorted(D.values(), key=lambda dep: dep["LEGISLATURAS"])

print "ordenados!"

@app.route("/")
def inicial ():
    pag = "História dos Deputados do Brasil"
    pag += "<ul>"
    link = url_for('listar', ordem="a", qte="20", p="1")
    pag += '<li><a href="%s">Ordem Alfabética</a></li>' % (link)
    link = url_for('listar', ordem="c", qte="20", p="1")
    pag += '<li><a href="%s">Ordem Cronológica</a></li>' % (link)
    return pag


@app.route("/listar/<ordem>/<qte>/<p>")
def listar(ordem, qte, p):
    if ordem == "a":
        lista = LISTAALFAB
    else:
        lista = LISTACRONO
    qte = int(qte)
    p = int(p)
    lista = lista[qte*p-qte:qte*p]   
    pag = "<ul>"
    for dep in lista:
        nome = dep["TXTNOME"]
        cod = dep["CODPESSOA"]
        link = url_for('dep', cod=cod)
        pag += '<li><a href="%s">%s</a></li>' % (link, nome)
    pag += "</ul>"
    link = url_for("listar", ordem=ordem, qte=str(qte), p=str(p+1))
    pag += '<a href="%s">Proximo</a>' % (link)
    return pag
    
@app.route("/dep/<cod>")
def dep(cod):
    dep = D[cod]
    idcad = dep["IDECADASTRO"]
    pag = '<img src="/static/fotos/%s.jpg"/>'% (idcad)
    pag += "<ul>"
    for tag, valor in dep.items():
        pag += "<li>%s: %s</li>" % (tag, valor)
    pag += "</ul>"   
    return pag




@app.route("/bethoven")
def bebe():
    return '<h1>Bethoven!</h1><img src="static/midia/bethoven.png">'










if __name__ == "__main__":
    app.run()

