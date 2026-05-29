"""
ASGI config for mitre_platform project.

This exposes the ASGI callable as a module-level variable named ``application``.
It enables asynchronous support and deployment through ASGI servers.
For more information, see https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/.
"""

import os
from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mitre_platform.settings')

application = get_asgi_application()