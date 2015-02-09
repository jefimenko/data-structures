from parens import parens

def test_balanced_parens():
    assert parens('(acds)(3resfds(weafdsa(asdf))(asd&*&))') is 0

def test_open_it_parens():
    assert parens('(32ruyefhasj()') is 1

def test_closed_parens():
    assert parens('(32refsad()))') is -1
