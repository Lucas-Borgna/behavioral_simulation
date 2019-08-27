import unittest
import os
import glob
import sys
import xunitparser
import argparse

class CocotbResultsBase(unittest.TestCase):
	
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

	@staticmethod
	def setUp():
		basedir = CocotbResultsBase.__location__
		results_path = os.path.join(basedir, CocotbResultsBase.args.results)
		file_path = glob.glob(os.path.join(results_path, 'results.xml'))
		print(file_path)
		return file_path


class TestCocotbResults(CocotbResultsBase):
	
 
	def test_setUp(self):
		xmlfile_path = self.setUp()
		
		print(xmlfile_path)
		if len(xmlfile_path) == 0:
			raise IOError('Cannot find the results.xml file. Searched in"{0:s}"'.format(CocotbResultsBase.args.results))
		
	def test_anyFailures(self):
		xmlfile_path = self.setUp()
		testSuites, testResults = xunitparser.parse(open(xmlfile_path[0]))
		print(testResults.wasSuccessful())
		
		self.assertTrue(testResults.wasSuccessful(), msg = "There were failures in cocotb tests, inspect results.xml file")



if __name__ == '__main__':

		
	parser = argparse.ArgumentParser(description='check test cases for cocotb results')
	parser.add_argument('-r','--results', required = True, metavar = 'results', type=str, help='input results xml folder')
	args, remaining_args = parser.parse_known_args()

	CocotbResultsBase.args = args
	print(args)
	print(remaining_args)
	print(sys.argv[:1])

	unittest.main(argv=sys.argv[:1] + remaining_args)



