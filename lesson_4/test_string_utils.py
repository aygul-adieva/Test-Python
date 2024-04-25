import pytest
from string_utils import StringUtils

@pytest.mark.positive_test_capitilize

@pytest.mark.parametrize('line, result', [("привет", "Привет"), ('123', "123"), ("добрый день"), "Добрый день"])
def test_positive_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result

@pytest.mark.skip
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('line, result', [("",""),(" ", " "), (None, None)])
def test_negative_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res ==result
