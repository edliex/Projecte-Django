# Projecte de Django

## Introducció
Aquest és un projecte per fer una aplicació web utilitzant el framework Django, on el principal objectiu de la web és una xarxa de blogs de programació, on pots veure diferents notícies i tutorials.

## Instal·lació ràpida
1. Primer hem d'obrir el terminal i clonar el repositori amb la comanda:
   `git clone https://github.com/edliex/Projecte-Django.git`
2. Després entrem dins amb la comanda `cd Projecte-Django`
3. Ara preparem un entorn virtual amb la comanda `python -m venv env_site`
4. Activem l'entorn virtual amb la comanda `.\env_site\Scripts\activate.ps1`
5. Després instal·lem les dependències necessàries amb `python -m pip install django Pillow`
6. Abans d'iniciar el servidor, hem d'aplicar les migracions a la base de dades amb `python manage.py makemigrations` i `python manage.py migrate`

## Execució del projecte
1. Per últim, utilitzem `python manage.py runserver` per activar l'aplicació web.
2. Podrem accedir a través de l'URL `http://127.0.0.1:8000`

## Pydocs
1. Views.py: https://edliex.github.io/Projecte-Django/blog.views.html
2. Models.py: https://edliex.github.io/Projecte-Django/blog.models.html
