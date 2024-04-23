import pytest
from string_utils import StringUtils

@pytest.mark.positive_test_capitilize

@pytest.mark.parametrize('line, result', [("привет", "Привет"), ('123', "123"), ("Добрый день"), "Добрый день"])
def test_positive_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_capitalize
@pytest.mark.parametrize('line, result', [("",""),(" ", " "), (None, None)])
def test_negative_capitalize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(line)
    assert res ==result
