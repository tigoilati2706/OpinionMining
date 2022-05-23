from init import app
from Controller.auth import *
from Controller.Admin import *
from Controller.User import *
# from Controller.User import create_app
# app = create_app()
# app.app_context().push()
#app.run(host='localhost', port=5000,debug = True, threaded = True, use_reloader = False)


app.run(host='0.0.0.0', port=5000,debug = True, threaded = True, use_reloader = False)
