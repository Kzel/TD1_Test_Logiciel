import funcs
import unittest

db_path = 'ex2.db'

class TestFuncs(unittest.TestCase):
	def test_add_user(self):
		self.assertEqual(funcs.add_user(db_path,'BA!','1234567','this is spublickey1','this is sprivatekey1', 'this is epublickey1', 'thisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekeythisiseprivatekey'), True)
		self.assertEqual(funcs.add_user(db_path,'YiningBAO','Ab!123456','this is spublickey2','this is sprivatekey2', 'this is epublickey2', 'this is eprivatekey2'), True)
  
	
if __name__ == '__main__':
    funcs.drop_db(db_path)
    funcs.create_db(db_path)
    unittest.main()