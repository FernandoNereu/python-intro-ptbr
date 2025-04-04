import pytest
from hello import main

def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, World! CI/CD Test Successful!" in captured.out