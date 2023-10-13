from nimnim import nim


def test_empty_string():
    assert nim("") == ""


def test_single_word():
    assert nim("foo") == "F"


def test_sentence_with_stop_words():
    assert nim("here and there") == "HT"


def test_only_stop_words():
    assert nim("the and of") == ""
