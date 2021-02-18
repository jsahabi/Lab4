import driver


def letter(row, col):
    if row == 20 and col == 20:
        return 'A'


if __name__ == '__main__':
    driver.comparePatterns(letter(20, 20))

