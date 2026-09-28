def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def test_simple_interest():
    result = calculate_simple_interest(1000, 5, 2)
    assert result == 100


def test_zero_principal():
    result = calculate_simple_interest(0, 5, 2)
    assert result == 0
