"""
This is an example test module.
"""
from repo_a.module_a import hello
from repo_b import main as repo_b_main
from repo_c import main as repo_c_main

def test_hello():
    """
    This is an example test function.
    """
    assert hello() == "Hello from module_a"


def test_module_b_main(capsys):
    """
    Test the main function from module B.
    """
    repo_b_main()

def test_module_c_main(capsys):
    """
    Test the main function from module C.
    """
    repo_c_main()



