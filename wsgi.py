# esse kra faz a ligação entre o apache e o python

import sys

sys.path.insert(0, "/var/www/webroot/ROOT")


from app import app as application
