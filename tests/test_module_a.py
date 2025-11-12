"""
This is an example test module.
"""
from module_a import hello
from repo_b import main as repo_b_main

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



