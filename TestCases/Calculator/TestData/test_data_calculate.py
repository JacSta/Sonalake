def calculations():
    return {
        "first_calc": ['3', '5', 'Mult', '9', '9', '9', 'Plus', 'ParanL', '1', '0', '0', 'Div', '4', 'ParanR', 'Calc'],
        "second_calc": ['Cos', 'Pi', 'ParanR', 'Calc'],
        "third_calc": ['Sqrt', '8', '1', 'ParanR', 'Calc']
    }


def expected_results():
    return {
        "first_calc": "34990",
        "second_calc": "-1",
        "third_calc": "9"
    }


def expected_calc():
    return ['35*999+(100/4)', 'cos(pi)', 'sqrt(81)']
