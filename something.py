
# @main.route('/servershutdowntest.py')
# def server_shutdown():
# 	if not current_app.testing:
# 		abort(404)
# 	shutdown=request.environ.get('werkzeug.server.shutdown')
# 	if not shutdown:
# 		abort(500)
# 	shutdown()
# 	return 'shutting down...'		