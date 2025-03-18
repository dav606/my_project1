import pytest


@pytest.fixture(scope='function')
def simple_print_function_scope():

    print("Function scope")

@pytest.fixture(scope='session')
def simple_print_session_scope():
    print("Session scope")



