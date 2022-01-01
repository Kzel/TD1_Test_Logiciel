import funcs
import unittest

db_path = 'ex2.db'

class TestFuncs(unittest.TestCase):
	def test_add_user(self):
		self.assertEqual(funcs.add_user(db_path,'BA!','1234567','this is spublickey1'.rjust(128)[:128],'this is sprivatekey1'.rjust(128)[:128], 'this is epublickey1'.rjust(128)[:128], 'this is eprivatekey1'.rjust(129)[:129]), True)
		self.assertEqual(funcs.add_user(db_path,'YiningBAO','Ab!123456','this is spublickey2'.rjust(128)[:128],'this is sprivatekey2'.rjust(128)[:128], 'this is epublickey2'.rjust(128)[:128], 'this is eprivatekey2'.rjust(128)[:128]), True)
  
	def test_login(self):
		self.assertEqual(funcs.log(db_path,'BA!','Ab!123456'), False)
		self.assertEqual(funcs.log(db_path,'YiningBAO','Ab!123456'), True)
	
	def test_password(self):
		self.assertEqual(funcs.get_password(db_path,'BA!'), '1234567')
		self.assertEqual(funcs.get_password(db_path, 'YiningBAO'), 'Ab!123456')
  
	def test_spublickey(self):
		self.assertEqual(funcs.get_spubkey(db_path,'BA!'),'this is spublickey1'.rjust(128)[:128])
		self.assertEqual(funcs.get_spubkey(db_path,'YiningBAO'),'this is spublickey2'.rjust(128)[:128])
	
	def test_sprilickey(self):
		self.assertEqual(funcs.get_sprikey(db_path,'BA!'),'this is sprivatekey1'.rjust(128)[:128])
		self.assertEqual(funcs.get_sprikey(db_path,'YiningBAO'),'this is sprivatekey2'.rjust(128)[:128])
	
	def test_epublickey(self):
		self.assertEqual(funcs.get_epubkey(db_path,'BA!'),'this is epublickey1'.rjust(128)[:128])
		self.assertEqual(funcs.get_epubkey(db_path,'YiningBAO'),'this is epublickey2'.rjust(128)[:128])
	
	def test_eprilickey(self):
		self.assertEqual(funcs.get_eprikey(db_path,'BA!'),'this is eprivatekey1'.rjust(129)[:129])
		self.assertEqual(funcs.get_eprikey(db_path,'YiningBAO'),'this is eprivatekey2'.rjust(128)[:128])
  
	def test_verify_username_length(self):
		self.assertEqual(funcs.verify_username_length(db_path,'BA!'), False)
		self.assertEqual(funcs.verify_username_length(db_path,'YiningBAO'), True)
	
	def test_verify_username_special_characters(self):
		self.assertEqual(funcs.verify_username_special_characters(db_path,'BA!'), True)
		self.assertEqual(funcs.verify_username_special_characters(db_path, 'YiningBAO'), False)
  
	def test_verify_key_length(self):
		self.assertEqual(funcs.verify_key_length(db_path,'BA!'), False)
		self.assertEqual(funcs.verify_key_length(db_path,'YiningBAO'), True)
  
	def test_verify_password(self):
		self.assertEqual(funcs.verify_password(db_path,'BA!'), False)
		self.assertEqual(funcs.verify_password(db_path,'YiningBAO'), True)
	
if __name__ == '__main__':
    funcs.drop_db(db_path)
    funcs.create_db(db_path)
    unittest.main()