import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)
  
	def test_min_int(self):
		self.assertEqual(funcs.min_int(1, 5), 1)
		self.assertEqual(funcs.min_int(-3, -1), -3)
		self.assertEqual(funcs.min_int(-5, 5), -5)
		self.assertEqual(funcs.min_int(0, 0), 0)
  
	def test_average_func(self):
		self.assertEqual(funcs.average([1, 2, 3, 4, 5]), 3)
		self.assertEqual(funcs.average([2, 4, 6, 8, 10]), 6)
		self.assertEqual(funcs.average([2, 2, 2, 2, 2, 2, 2]), 2)
		self.assertEqual(funcs.average([5, 2, 3, 7, 8, 9, 1, 3, 8, 9]),5.5)
  
	def test_std_func(self):
		self.assertEqual(funcs.std([1, 2, 3, 4, 5]), 1.41)
		self.assertEqual(funcs.std([2, 4, 6, 8, 10]), 2.83)
		self.assertEqual(funcs.std([1, 2, 5, 6, 7, 8]), 2.54)
		self.assertEqual(funcs.std([1, 2, 3, 4, 7, 8]), 2.54)
  
	def test_mediane_func(self):
		self.assertEqual(funcs.mediane([1, 2, 3, 4, 5]), 3)
		self.assertEqual(funcs.mediane([6, 4, 2, 8, 10]), 6)
		self.assertEqual(funcs.mediane([5, 2, 1, 6, 7, 8]), 5.5)
		self.assertEqual(funcs.mediane([4, 2, 3, 1, 7, 8]), 3.5)

if __name__ == '__main__':
	unittest.main()