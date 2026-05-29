#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script serves as the entry point for various Django administrative
commands, such as starting the development server or performing database
migrations. It is intentionally kept simple so that newcomers can
understand how Django projects are executed. If you need more
customization, you can refer to the official Django documentation.
"""
import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mitre_platform.settings')
    try:
        from django.core.management import execute_from_command_line  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your "
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()