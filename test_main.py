"""
Author: Ajay Shimpi

NOTE:
1. install venv
2. activate venv
3. python3 install pytest
4. compiler c code
gcc -shared -o main.so main.c
5. run pytest
py -m pytest -v -s
6. to generate html form:
 [make sure coverage is installed]
 py -m pip install coverage

 py -m coverage run -m pytest
 py -m coverage html

 results -> Open the htmlcov/index.html  
 NOTE, Link: https://coverage.readthedocs.io/en/7.6.1/

 Alternative : py -m pytest --cov=. --cov-report=html
7. optional: 
py -m coverage report -m

result -> 
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
test_main.py      30     17    43%   34-37, 55-56, 59-60, 67, 71, 73-82, 100
--------------------------------------------
TOTAL             30     17    43%

7.[make sure gcovr is installed
py -m pip install gcovr]
py -m gcovr -r . --html --html-details -o coverage.html

8. coverage.info -> optional
py -m pytest --cov=. --cov-report=lcov:coverage.info
py -m coverage lcov -o coverage.info


"""

import ctypes
from ctypes import CDLL
import pytest
import unittest
import os

# Load shared library
#main = ctypes.CDLL("./main.dll") #.dll can be use as per generated file from 'gcc -shared -o main.dll main.c'
main = ctypes.CDLL("./main.so")
"""
add below condition later -->
# Check if 'main.so' or 'main.dll' exists
file_names = ['./main.so', './main.dll']
existing_files = [file for file in file_names if os.path.exists(file)]
"""


@pytest.fixture
def libmain():
    yield CDLL('./main.so')

def test_Add():
    print("test_add (outside class) called...!\n")
    assert main.add(4,5) == 9

def test_add2(libmain):
    print("test_add2 (outside class) called...!\n")
    assert libmain.add(4,7) == 11
    assert libmain.add(10,5) == 15
    # assert libmain.add(20,5) == 5, f"Invalid sum result" # trial for failed TC
    assert libmain.add(30,5) == 35


# test cases, class
class TestMain(unittest.TestCase):

    # setUp
    def setUp(self):
        print("setUp (inside class) called...!\n")
        self.a = 10
        self.b = 5
        #self.main = ctypes.CDLL('./main.so')

    # First Test case
    def test_add(self):
        print("test_add (inside class) called...!")
        self.assertEqual(main.add(self.a, self.b), 15)

if __name__ == '__main__':
    unittest.main()


"""# Load the shared library into c types.
if sys.platform.startswith('win'):
    c_lib = ctypes.CDLL(libname / "main.dll")
else:
    c_lib = ctypes.CDLL(libname / "main.so")

# sample data for call
x,y = 5, 6.5

c_lib.add.restype = ctypes.c_float
answer = c_lib.add(x, ctypes.c_float(y))
print(f"    In python : int: {x} float: {y:.1f} return val {answer:.1f}")
"""


"""
INFO:

python -m pip install -r requirements.txt
"""