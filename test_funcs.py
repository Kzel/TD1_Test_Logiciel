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

 
	def test_arithmetic_func(self):
		self.assertEqual(funcs.arithmetic([1, 3, 9, 27, 81]), False)
		self.assertEqual(funcs.arithmetic([2, 4, 6, 8, 10]), True)
		self.assertEqual(funcs.arithmetic([2, 4, 8, 16, 32, 64]), False)
		self.assertEqual(funcs.arithmetic([1, 2, 3, 4, 5, 6]), True)
  
	def test_geometric_func(self):
		self.assertEqual(funcs.geometric([1, 3, 9, 27, 81]), True)
		self.assertEqual(funcs.geometric([2, 4, 6, 8, 10]), False)
		self.assertEqual(funcs.geometric([2, 4, 8, 16, 32, 64]), True)
		self.assertEqual(funcs.geometric([1, 2, 3, 4, 7, 8]), False)
  
	def test_arithmeticN_func(self):
		self.assertEqual(funcs.arithmeticN([1, 3, 9, 27, 81], 3), False)
		self.assertEqual(funcs.arithmeticN([2, 4, 6, 8, 10], 3), (True, [12.0, 14.0, 16.0]))
		self.assertEqual(funcs.arithmeticN([2, 4, 8, 16, 32, 64], 3), False)
		self.assertEqual(funcs.arithmeticN([1, 2, 3, 4, 5, 6], 3) , (True, [7.0, 8.0, 9.0]))
  
	def test_geometricN_func(self):
		self.assertEqual(funcs.geometricN([1, 3, 9, 27, 81], 3), (True, [243.0, 729.0, 2187.0]))
		self.assertEqual(funcs.geometricN([2, 4, 6, 8, 10], 3), False)
		self.assertEqual(funcs.geometricN([2, 4, 8, 16, 32, 64], 3), (True, [128.0, 256.0, 512.0]))
		self.assertEqual(funcs.geometricN([1, 2, 3, 4, 7, 8], 3), False)
  
if __name__ == '__main__':
	unittest.main()