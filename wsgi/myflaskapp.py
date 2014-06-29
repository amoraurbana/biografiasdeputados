import os 
import xml.etree.ElementTree as ET
from flask import Flask
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
#print D


@app.route("/")
def todos():
    pag = "<ul>"
    for cod, dep in D.items():
        nome = dep["TXTNOME"]
        pag += '<li><a href="dep/%s">%s</a></li>' % (cod, nome)
    pag += "</ul>"   
    return pag
    
@app.route("/dep/<cod>")
def lista(cod):
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

