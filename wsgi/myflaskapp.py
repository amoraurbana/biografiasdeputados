import xml.etree.ElementTree as ET
from flask import Flask
app = Flask(__name__)

diretorio = __file__.rpartition("/")[0]
raiz = ET.parse(diretorio+"/static/bios/0.xml")
deps = raiz.findall("./DATA_RECORD")

D = {}
for dep in deps:
    cod = dep.find("CODPESSOA").text
    crian = dep.getchildren()
    d = {}
    for c in crian:
        d[c.tag] = c.text
    D[cod] = d
    
print D


@app.route("/")
def todos():
    pag = ""
    for dep in D.values():
        pag += dep["TXTNOME"]
    return pag




@app.route("/bethoven")
def bebe():
    return '<h1>Bethoven!</h1><img src="static/midia/bethoven.png">'










if __name__ == "__main__":
    app.run()

