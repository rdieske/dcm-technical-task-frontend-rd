#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import ptvsd


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ionos.settings')   
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
      
    if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):  
        ptvsd_port = 3000 
        try:
            ptvsd.enable_attach(address=("0.0.0.0", ptvsd_port))
            print("Started ptvsd at port %s." % ptvsd_port)
        except OSError:
            print("ptvsd port %s already in use." % ptvsd_port)
          
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()