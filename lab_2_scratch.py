from math import isclose


def compute_tax(price, tax_rate=0.08):
    """
    Computes the amount of tax owed on a purchase.
    :param price: A positive number.
    :param tax_rate: A positive float.
    :return: A number.
    """

    if price or tax_rate < 0:
        raise ValueError('Cannot have negative price')
    return price * tax_rate


def get_tax_by_state(state_name):
    if state_name == 'Oregon':
        tax_rate = 0.0
    elif state_name == 'Illinois':
        tax_rate = 0.08
    elif state_name == 'Texas':
        tax_rate = 0.25

    return tax_rate


if __name__ == '__main__':

    try:
        should_expect = compute_tax(-5, 0.20)  # Code that's looking for exception
        print('Our code failed to except properly')
    except ValueError:
        print('Our code excepted properly')

    my_price = 0.80
    expected_tax = 0.16
    computed_tax = compute_tax(my_price, 0.20)

    if isclose(computed_tax, expected_tax, abs_tol=1e-8):
        print('Test looks good')
    else:
        print('Test failed')

compute_tax(3, 1)
