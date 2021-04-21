"""
WSGI config for save_a_word project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

try:
	from dotenv import load_dotenv

	project_folder = os.path.expanduser('~/SaveAWord/Save_a_word_server')  # adjust as appropriate
	load_dotenv(os.path.join(project_folder, '.env'))
except Exception as e:
	print(e)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'save_a_word.settings')

application = get_wsgi_application()
