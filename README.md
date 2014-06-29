Biografias Deputados (Brasil)
==================

Usando base de dados da Câmara dos Deputados, fizemos esse proto-site para disponibilizar as infos que não estavam disponíveis ao público.

Atualmente este sistema está hospedado aqui:
deputados-nascidades.rhcloud.com

Este código está sob licença GPL3.



Running on OpenShift
----------------------------

Create an account at https://www.openshift.com

Create a python application

    rhc app create deputados python-2.6

Add this upstream repo

    cd deputados
    git remote add upstream -m master https://github.com/amoraurbana/biografiasdeputados.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://deputados-$yournamespace.rhcloud.com
