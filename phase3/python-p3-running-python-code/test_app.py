# test_app.py

import sys
sys.path.append('lib')  # Add the lib folder to the path

def test_hello_output(capsys):
    import app  # This runs the print() in app.py
    captured = capsys.readouterr()
    assert captured.out == "Hello World! Pass this test, please.\n"
