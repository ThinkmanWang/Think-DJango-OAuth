#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

'''
curl -X POST -d "grant_type=password&username=root&password=Ab123145" -u"9AQhtuuEh1bcbQ2HRmTumL8DX9UM8xGYZqZL5xOB:T1G7vtOLkJCyYNtsEzjFqaLm6n2LuvYGP823lmQlgMWtQk9kRudoilsOavQ1JUDxWFGYLUR9a6ZOX7MokI2taluLxz0BQHWzrFiCe9DAFtW2pIkxKijax1hscITIoXmP" http://localhost:8000/o/token/
curl -H "Authorization: Bearer ESRNnksyKXs1jNXy7KJMMLz4qFV3OC" http://localhost:8000/api/hello
'''

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'console.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
