import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IN16_Study_Manager.settings')

application = get_wsgi_application()

# Vercel expects the WSGI app to be called "app"
app = application
