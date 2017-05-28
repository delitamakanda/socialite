import unittest
import re
import threading
import time
from selenium import webdriver
from app import create_app, db
from app.models import User, Role, Post, Permission

class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        #start Chrome
        try:
            cls.client = webdriver.Chrome()
        except:
            pass

        if cls.client:
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()


            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")

            db.create_all()
            Role.insert_roles()
            User.generate_fake(100)
            Post.generate_fake(100)

            admin_role = Role.query.filter_by(permissions=0xff).first()
            admin = User(email='pamplemouse.rose@example.com', username='pamplemouse', password='test', role=admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            threading.Thread(target=cls.app.run).start()

        @classmethod
        def tearDownClass(cls):
            if cls.client:
                cls.client.get('http://localhost:5000/shutdown')
                cls.client.stop()

                db.drop_all()
                db.session.remove()

                cls.app_context.pop()

        def setUp(self):
            if not self.client:
                self.skipTest('Web browser not available')

        def tearDown(self):
            pass

        def test_admin_home_page(self):
            self.client.get('http://localhost:5000/')
            self.assertTrue(re.search('Hello,\s+Stranger!', self.client.page_source))
            self.client.find_element_by_link_text('Sign in').click()
            self.assertTrue('<h1>Login</h1>' in self.client.page_source)


            self.client.find_element_by_name('email').send_keys('pamplemouse.rose@example.com')
            self.client.find_element_by_name('password').send_keys('test')
            self.client.find_element_by_name('submit').click()
            self.assertTrue(re.search('Hello,\s+pamplemouse!', self.client.page_source))

            self.client.find_element_by_link_text('Profile').click()
            self.assertTrue('<h1>pamplemouse</h1>' in self.client.page_source)
