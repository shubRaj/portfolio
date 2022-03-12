import os
os.system(f"gunicorn portfolio.wsgi -b=127.0.0.1:8002 --workers=2 --threads=6 --daemon")