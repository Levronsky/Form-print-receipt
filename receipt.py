PRODUCTS = [
    # for example
    ['apples', 100],
    ['swiss cheese', 1500],
    ['red fish', 450],
    ['cold smoked grouped', 12400],
]


def create_formatted_receipt(products):
    '''Form a check for printing.

    The function argument is a shopping list,
    consisting of the product name and price.
    As a result, check lines are formed for
    output to the screen and subsequent printing.
    The function itself does not call "print".
    '''
    receipt_lines = []
    check_width = 30
    name_max_width = 17
    name_cropp = 14
    delimiter_top = (' ' + ('_' * check_width)
                     + '\n|' + (' ' * check_width) + '|')
    receipt_lines.append(delimiter_top)
    for product, price in products:
        if len(product) > name_max_width:
            product = product[:name_cropp] + '...'
        receipt_lines.append(
                ("|{:<20}{:>10}|").
                format(product, price)
                )
    delimiter_bottom = '|' + ('_' * check_width) + '|'
    receipt_lines.append(delimiter_bottom)
    return receipt_lines


def print_all_lines(lines):
    for line in lines:
        print(line)


if __name__ == '__main__':
    receipt = create_formatted_receipt(PRODUCTS)
    print_all_lines(receipt)
