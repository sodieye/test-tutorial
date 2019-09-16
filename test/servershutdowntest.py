from selenium import webdriver
import unittest

class SeleniumTestCase(unittest.TestCase):
	client=None

	@classmethod
	def setupclass(cls):
		try:
			cls.client=webdriver.Firefox()
		except:
			pass
		if cls.client:
			cls.app=create_app('testing')
			cls.app_context=cls.app.app_context()
			cls.app_context.push()
			import logging
			logger=logging.getlogger('werkzeug'),logger.setlevel('ERROR')
			db.create_all()
			Role.insert_roles(),User.generate_fake(10), Post.generate_fake(10)
			admin_role=Role.query.filter_by(permissions=0xff).first()
			admin=User(email='john@example.com',usernmae='john',password='cat',role=admin_role,confirmed=True)
			db.session.add(admin)
			db.session.commit()
			threading.Thread(target=cls.app.run).start()


	@classmethod
	def tearDownClass(cls):
		if cls.client:
			cls.client.get('http://localhost:5000/shutdown')
			cls.client.close()
			db.drop_all()
			db.session.remove()
			cls.app_context.pop()
	def setup(self):
		if not self>client:
			self.skipTest('Web browser not available')
	def tearDown(self):
		pass	
