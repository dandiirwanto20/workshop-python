# Build and Install

# $ pip install wheel

# $ python setup.py bdist_wheel

# $ pip install flaskr-1.0.0-py3-none-any.whl

# Bash

"""
$ export FLASK_APP=flaskr
$ flask init-db
"""
# Fish

"""
$ set -x FLASK_APP flaskr
$ flask init-db
"""
# CMD

"""
> set FLASK_APP=flaskr
> flask init-db
"""
# PowerShell

"""
> $env:FLASK_APP = "flaskr"
> flask init-db
"""

# Configure the Secret Key

"""
$ python -c 'import secrets; print(secrets.token_hex())'

'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

"""

# Run with a Production Server

#Instead, use a production WSGI server. For example, to use Waitress, first install it in the virtual environment:

# $ pip install waitress

# $ waitress-serve --call 'flaskr:create_app'

# Serving on http://0.0.0.0:8080