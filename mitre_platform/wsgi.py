"""
WSGI config for mitre_platform project.

This exposes the WSGI callable as a module-level variable named ``application``.
It is used by Django's development server and any production WSGI deployments.
For more information, see https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/.
"""

import os
from django.core.wsgi import get_wsgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mitre_platform.settings')

application = get_wsgi_application()