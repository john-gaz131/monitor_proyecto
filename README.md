# Monitor del Sistema (Django + psutil)

Aplicación web que muestra en tiempo real el uso de CPU, RAM, Disco y la información del sistema operativo.

## Requisitos
- Python 3.10 o superior
- pip
- (Recomendado) entorno virtual

## Instalación
```bash
git clone <url-del-repo>
cd monitor_proyecto              
python -m venv venv && venv\Scripts\activate   
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
