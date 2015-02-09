from parens import balanceness

def test_balanced():
    # Simple case.
    assert balanceness(u'()') is 0
    # Extension of the simple case.
    assert balanceness(u'((()))') is 0
    # Empty string is considered 'balanced'
    assert balanceness(u'') is 0

def test_balanced_longer():
    assert balanceness(u'()()') is 0
    assert balanceness(u'()()(())') is 0
    assert balanceness(u'()(()())') is 0
    assert balanceness(u'()(())()') is 0


def test_open():
    assert balanceness(u'(') is 1
    assert balanceness(u'(()') is 1


def test_open_longer():
    assert balanceness(u'(())(') is 1
    assert balanceness(u'()()(') is 1


def test_broken():
    assert balanceness(u')') is -1
    assert balanceness(u'())') is -1
    assert balanceness(u')()') is -1


def test_broken_longer():
    assert balanceness(u')))(((') is -1
    assert balanceness(u'((())))') is -1
    assert balanceness(u'()())()') is -1