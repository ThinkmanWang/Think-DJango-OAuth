#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

'''
curl -X POST -d "grant_type=password&username=root&password=Ab123145" -u"xylTl8sQQIjhTvcPgLx5oKeV52HvBdKgqYAEUgRC:C26vMbUReltXnDwOLUA9Vr8POR9PjDdAzo8jndDcbEP10UM4bF3DdeGwBW3t7vdWlhWaQW5b1ctMN5IfKn43Vobl15b8w0ZgBW97oAdMZH3IQwA7jNpmBvF76QYi5zfG" http://localhost:8000/o/token/
curl -H "Authorization: Bearer HxW4UUDaq6Hibafrs5aPNVk4uUpPR7" http://localhost:8000/api/hello
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
