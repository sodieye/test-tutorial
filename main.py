from flask import Blueprint,render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():

    return render_template('profile.html',name=current_user.name)

@main.route('/servershutdowntest.py')
def server_shutdown():
	if not current_app.testing:
		abort(404)
	shutdown=request.environ.get('werkzeug.server.shutdown')
	if not shutdown:
		abort(500)
	shutdown()
	return 'shutting down...'		
