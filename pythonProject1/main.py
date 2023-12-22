from ComplexNumClass import ComplexNumber


if __name__ == '__main__':
    print("Beginning of the ComplexNumber class trial...")

    z1 = ComplexNumber(3, 4)

    # z2 = z1 + (4+5j) + (7+3j) + z1 = 17 + 16j
    z2 = z1.addition((4, 5), (7, 3), z1)

    # z3 = z2 - (2 * z1) = 11 + 8j
    z3 = z2.subtraction(z1.multiplication((2, 0)))

    z4 = z3.multiplication((0, 1))

    z5 = ComplexNumber(16, -24)
    z6 = ComplexNumber(2, 0)
    z7 = z5.division(z6, z6, (2, 0))

    z7.division((0, -1))

    print("The end of the ComplexNumber class trial.")
