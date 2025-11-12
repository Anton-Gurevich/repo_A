"""
This is an example test module.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from module_a import hello

def test_hello():
    """
    This is an example test function.
    """
    assert hello() == "Hello from module_a"

