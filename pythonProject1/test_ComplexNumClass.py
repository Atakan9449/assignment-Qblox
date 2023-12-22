import unittest
from unittest import TestCase
from ComplexNumClass import ComplexNumber


test_z1 = ComplexNumber(1, 2)
test_z2 = ComplexNumber(-3, 3)
test_tuple = (1, -4)


class TestComplexNumber(TestCase):
    def test_addition(self):
        """
        Tests addition method of ComplexNumber class

        Requirements:
            1- The method should return an object of ComplexNumber class \n
            2- The attributes of the class should be verified that operation can be executed correctly \n
            2- The method should raise TypeError exception if wrong arguments given \n
            3- The method should raise ValueError exception if no argument given \n

        TestCases:
            1- assertIsInstance: to verify returned object's type \n
            2- assertEqual x2: to verify real and imaginary attributes of the object (algorithm check) \n
            3 and 4- assertRaises x2: to verify parameter types \n
        """
        print("\nAddition method test is beginning...")
        # Addition method returns an object,
        # Each attribute of returned object is tested separately
        # Both of the argument options(class and tuple) are given at the same time to increase complexity
        self.assertIsInstance(test_z1.addition(test_z2, test_tuple), ComplexNumber)

        # 1 + (-3) + 1 = -1 (real numbers)
        self.assertEqual(test_z1.addition(test_z2, test_tuple).real, -1)

        # 2 + 3 + (-4) = 1 (imaginary numbers)
        self.assertEqual(test_z1.addition(test_z2, test_tuple).imag, 1)

        # if the argument of the function is not ComplexNumber object or tuple, throws exception
        # Members of test_tuple is given as integer to raise exception
        self.assertRaises(TypeError, test_z1.addition, 1, -4)
        self.assertRaises(ValueError, test_z1.addition)
        print("Addition method test has ended.\n")

    def test_subtraction(self):
        """
        Tests subtraction method of ComplexNumber class

        Requirements:
            1- The method should return an object of ComplexNumber class \n
            2- The attributes of the class should be verified that operation can be executed correctly \n
            2- The method should raise TypeError exception if wrong arguments given \n
            3- The method should raise ValueError exception if no argument given \n

        TestCases:
            1- assertIsInstance: to verify returned object's type \n
            2- assertEqual x2: to verify real and imaginary attributes of the object (algorithm check) \n
            3 and 4- assertRaises x2: to verify parameter types \n
        """
        print("\nSubtraction method test is beginning...")
        # Subtraction method returns an object,
        # Each attribute of returned object is tested separately
        # Both of the argument options(class and tuple) are given at the same time to increase complexity
        self.assertIsInstance(test_z1.subtraction(test_z2, test_tuple), ComplexNumber)

        # 1 - (-3) - 1 = 3 (real numbers)
        self.assertEqual(test_z1.subtraction(test_z2, test_tuple).real, 3)

        # 2 - 3 - (-4) = 3 (imaginary numbers)
        self.assertEqual(test_z1.subtraction(test_z2, test_tuple).imag, 3)

        # if the argument of the function is not ComplexNumber object or tuple, throws exception
        # Members of test_tuple is given as integer to raise exception
        self.assertRaises(TypeError, test_z1.subtraction, 1, -4)
        self.assertRaises(ValueError, test_z1.subtraction)
        print("Subtraction method test has ended.\n")

    def test_multiplication(self):
        """
        Tests multiplication method of ComplexNumber class

        Requirements:
            1- The method should return an object of ComplexNumber class \n
            2- The attributes of the class should be verified that operation can be executed correctly \n
            2- The method should raise TypeError exception if wrong arguments given \n
            3- The method should raise ValueError exception if no argument given \n

        TestCases:
            1- assertIsInstance: to verify returned object's type \n
            2- assertEqual x2: to verify real and imaginary attributes of the object (algorithm check) \n
            3 and 4- assertRaises x2: to verify parameter types \n
        """
        print("\nMultiplication method test is beginning...")
        # Multiplication method returns an object,
        # Each attribute of returned object is tested separately
        self.assertIsInstance(test_z1.multiplication(test_z2), ComplexNumber)

        # (1 * (-3)) - (2 * 3) = -9 (real number)
        self.assertEqual(test_z1.multiplication(test_z2).real, -9)

        # (1 * 3) + ((-3) * 2) = -3 (imaginary number)
        self.assertEqual(test_z1.multiplication(test_z2).imag, -3)

        # if the argument of the function is not ComplexNumber object or tuple, throws exception
        # Members of test_tuple is given as integer to raise exception
        self.assertRaises(TypeError, test_z1.multiplication, 1, -4)
        self.assertRaises(ValueError, test_z1.multiplication)
        print("Multiplication method test has ended.\n")

    def test_division(self):
        """
        Tests division method of ComplexNumber class

        Requirements:
            1- The method should return an object of ComplexNumber class \n
            2- The attributes of the class should be verified that operation can be executed correctly \n
            2- The method should raise TypeError exception if wrong arguments given \n
            3- The method should raise ValueError exception if no argument given \n

        TestCases:
            1- assertIsInstance: to verify returned object's type \n
            2- assertEqual x2: to verify real and imaginary attributes of the object (algorithm check) \n
            3 and 4- assertRaises x2: to verify parameter types \n
        """
        print("\nDivision method test is beginning...")
        # Division method returns an object,
        # Each attribute of returned object is tested separately
        self.assertIsInstance(test_z1.division(test_z2), ComplexNumber)

        # ((1 * (-3)) + (2 * 3)) / ((-3) ** 2 + 3 ** 2) = 1/6 (real number)
        self.assertEqual(test_z1.division(test_z2).real, 1/6)

        # ((2 * (-3)) - (1 * 3))) / ((-3) ** 2 + 3 ** 2) = -1/2 (imaginary number)
        self.assertEqual(test_z1.division(test_z2).imag, -1/2)

        # if the argument of the function is not ComplexNumber object or tuple, throws exception
        # Members of test_tuple is given as integer to raise exception
        self.assertRaises(TypeError, test_z1.division, 1, -4)
        self.assertRaises(ValueError, test_z1.division)
        print("Division method test has ended.\n")

    # TODO: add the entire polar plane functionality test in the TestComplexNumber class,
    #  after ComplexNumber class polar plane functionality completed


if __name__ == '__main__':
    unittest.main()
