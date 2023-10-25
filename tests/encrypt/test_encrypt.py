# from challenges.challenge_encrypt_message import encrypt_message
from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Test input valido
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("world", 2) == "dlr_ow"
    assert encrypt_message("abcde", 5) == "edcba"

    # Test key invalida
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hell", "hello")

    # Test menssagem invalida
    with pytest.raises(TypeError):
        encrypt_message(123, 4)

    # Test key exceeding message length
    assert encrypt_message("hello", 6) == "olleh"

    # Test odd key
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("world", 5) == "dlrow"

    # Test even key
    assert encrypt_message("hello", 4) == "o_lleh"
    assert encrypt_message("world", 6) == "dlrow"

    # Test empty string with key 1
    assert encrypt_message("", 1) == ""
