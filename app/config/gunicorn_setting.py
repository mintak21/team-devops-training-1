import os

# Sever Socket
host = '0.0.0.0'
port = os.getenv('PORT', 5000)

bind = str(host) + ':' + str(port)

# Debugging
reload = True

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'debug'

# Proc Name
proc_name = 'Flask-Local-Server'

# Worker Processes
workers = 1
worker_class = 'sync'