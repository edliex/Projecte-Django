# Projecte-Django
Projecte de Django
  Aquest es un projecte per fer una aplicacio web utilitzant el framework Django, on el principal objectiu de la web es una xarxa de blogs de programacio, on    pots veure diferents noticies i tutorials.

Preparacio:
  1. Primer hem d'obrir el terminal i clonar el repositori amb la comanda:
     git clone [https://github.com/edliex/Projecte-Django.git](https://github.com/edliex/Projecte-Django.git)
  2. Despres entrem dins amb 'cd Projecte-Django'
  3. Ara preparem un entorn virtual amb la comanda 'python -m venv env_site'
  4. Activem l'entor virtual amb la comanda '.\env_site\Scripts\activate.ps1'
  5. Despres instal·lem les depencencies necesaries amb 'python -m pip install django Pillow'
  6. Ara abans d'iniciar hem d'aplicar les migracions a la base de dades amb 'python manage.py makemigrations' i 'python manage.py migrate'
  7. Per ultim utilitzem 'python manage.py runserver' per activar la aplicacio web
  8. Podrem accedir a traves de l'URL 'http://127.0.0.1:8000'
 
Pydocs:
  1. Views.py: https://edliex.github.io/Projecte-Django/blog.views.html
  2. Models.py: https://edliex.github.io/Projecte-Django/blog.models.html
