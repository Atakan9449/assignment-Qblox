from __future__ import annotations


class ComplexNumber:
    """
    Generates a complex number object in cartesian coordinate with a+bj format.

    Current implementation supports 4 fundamental arithmetical operations in cartesian plane;
    addition, subtraction, multiplication and division.
    """
    # Constructor for the class
    def __init__(self, real_num: float, imag_num: float) -> None:
        """
        Constructor of ComplexNumber class.

        :param self: The object itself that is included in the operation
        :param float real_num: The real part of the complex number
        :param float imag_num: The imaginary part of the complex number
        :return: None
        """
        self.real = real_num
        self.imag = imag_num

    def addition(self, *args) -> ComplexNumber:
        """
        Performs addition of complex numbers in cartesian coordinate system and returns a complex number object.

        :param self: The object itself that is included in the operation
        :param args: A ComplexNumber object and/or a tuple to be included in the operation
        :return: A ComplexNumber object with real and imaginary values
        :rtype: ComplexNumber
        :raises ValueError: if the function has no given parameter
        :raises TypeError: if the function is given any parameter except tuple or ComplexNumber object
        """
        if not args:
            raise ValueError('The argument cannot be empty, should be ComplexNumber object and/or tuple')
        real = self.real
        imag = self.imag
        for arg in args:
            if isinstance(arg, tuple):
                real += arg[0]
                imag += arg[1]
            elif isinstance(arg, ComplexNumber):
                real += arg.real
                imag += arg.imag
            else:
                raise TypeError('The argument(s) of the method should be ComplexNumber object and/or tuple')
        if imag < 0:
            print(f'The result of addition is: {real}{imag}j')
        else:
            print(f'The result of addition is: {real}+{imag}j')
        return ComplexNumber(real, imag)

    def subtraction(self, *args) -> ComplexNumber:
        """
        Performs subtraction of complex numbers in cartesian coordinate system and returns a complex number object.

        :param self: The object itself that is included in the operation
        :param args: A ComplexNumber object and/or a tuple to be included in the operation
        :return: A ComplexNumber object with real and imaginary values
        :rtype: ComplexNumber
        :raises ValueError: if the function has no given parameter
        :raises TypeError: if the function is given any parameter except tuple or ComplexNumber object
        """
        if not args:
            raise ValueError('The argument cannot be empty, should be ComplexNumber object and/or tuple')
        real = self.real
        imag = self.imag
        for arg in args:
            if isinstance(arg, tuple):
                real -= arg[0]
                imag -= arg[1]
            elif isinstance(arg, ComplexNumber):
                real -= arg.real
                imag -= arg.imag
            else:
                raise TypeError('The argument(s) of the method should be ComplexNumber object and/or tuple')
        if imag < 0:
            print(f'The result of subtraction is: {real}{imag}j')
        else:
            print(f'The result of subtraction is: {real}+{imag}j')
        return ComplexNumber(real, imag)

    def multiplication(self, *args) -> ComplexNumber:
        """
        Performs multiplication of complex numbers in cartesian coordinate system and returns a complex number object.

        :param self: The object itself that is included in the operation
        :param args: A ComplexNumber object and/or a tuple to be included in the operation
        :return: A ComplexNumber object with real and imaginary values
        :rtype: ComplexNumber
        :raises ValueError: if the function has no given parameter
        :raises TypeError: if the function is given any parameter except tuple or ComplexNumber object
        """
        if not args:
            raise ValueError('The argument cannot be empty, should be ComplexNumber object and/or tuple')
        real = self.real
        imag = self.imag
        real_new = 0
        imag_new = 0
        for arg in args:
            if isinstance(arg, tuple):
                real_new = real*arg[0] - imag*arg[1]
                imag_new = real*arg[1] + imag*arg[0]
            elif isinstance(arg, ComplexNumber):
                real_new = real*arg.real - imag*arg.imag
                imag_new = real*arg.imag + imag*arg.real
            else:
                raise TypeError('The argument(s) of the method should be ComplexNumber object and/or tuple')
            real = real_new
            imag = imag_new
        if imag < 0:
            print(f'The result of multiplication is: {real}{imag}j')
        else:
            print(f'The result of multiplication is: {real}+{imag}j')
        return ComplexNumber(real, imag)

    def division(self, *args) -> ComplexNumber:
        """
        Performs multiplication of complex numbers in cartesian coordinate system and returns a complex number object.

        :param self: The object itself that is included in the operation
        :param args: A ComplexNumber object and/or a tuple to be included in the operation
        :return: A ComplexNumber object with real and imaginary values
        :rtype: ComplexNumber
        :raises ValueError: if the function has no given parameter
        :raises TypeError: if the function is given any parameter except tuple or ComplexNumber object
        """
        if not args:
            raise ValueError('The argument cannot be empty, should be ComplexNumber object and/or tuple')
        real = self.real
        imag = self.imag
        real_new = 0
        imag_new = 0
        for arg in args:
            if isinstance(arg, tuple):
                denominator = pow(arg[0], 2) + pow(arg[1], 2)
                real_new = (real * arg[0] + imag * arg[1]) / denominator
                imag_new = (imag * arg[0] - real * arg[1]) / denominator
            elif isinstance(arg, ComplexNumber):
                denominator = pow(arg.real, 2) + pow(arg.imag, 2)
                real_new = (real * arg.real + imag * arg.imag) / denominator
                imag_new = (imag * arg.real - real * arg.imag) / denominator
            else:
                raise TypeError('The argument(s) of the method should be ComplexNumber object and/or tuple')
            real = real_new
            imag = imag_new
        if imag < 0:
            print(f'The result of division is: {real}{imag}j')
        else:
            print(f'The result of division is: {real}+{imag}j')
        return ComplexNumber(real, imag)

    # TODO: add the entire polar plane functionality in the ComplexNumber class
