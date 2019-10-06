import unittest
from homework import Rectangle
import math


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle
        self.normal_rect = Rectangle(2, 4)
        self.sqr = Rectangle(2, 2)
        self.invalid_args = ((0, 0), (-1, -1), (-1, 0),
                             (0, -1), (1, 0), (0, 1),
                             (1, -1), (-1, 1))
        self.ctrl_rect_diag = math.sqrt(
            math.pow(self.normal_rect.height, 2) +
            math.pow(self.normal_rect.width, 2))
        self.ctrl_sqr_diag = math.sqrt(
            math.pow(self.sqr.height, 2) +
            math.pow(self.sqr.width, 2))

    def tearDown(self) -> None:
        del self.rect

    def test_invalid_params(self):
        for args in self.invalid_args:
            with self.subTest(args=args):
                self.assertRaises(ValueError, self.rect, *args)

    def test_unexpected_errors(self):
        for args in zip(range(1, 8, 2), range(8, 1, -2)):
            try:
                self.rect(*args)
            except Exception as er:
                self.fail(f'Unexpected error "{type(er)}" happened with args: {args}')

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.normal_rect.get_rectangle_perimeter(), 12)

    def test_get_rectangle_square(self):
        self.assertEqual(self.normal_rect.get_rectangle_square(), 8)

    def test_get_sum_of_corners(self):
        sum_of_corn = self.normal_rect.get_sum_of_corners
        invalid_num_of_corn = [-1, 0, 5]

        for val in invalid_num_of_corn:

            with self.subTest(val=val):
                self.assertRaises(ValueError, sum_of_corn, val)

        for val in range(1, 5):
            with self.subTest(val=val):
                self.assertEqual(sum_of_corn(val), val*90)

    def test_get_rectangle_diagonal(self):
        inst_rect_diag = self.normal_rect.get_rectangle_diagonal()
        inst_sqr_diag = self.sqr.get_rectangle_diagonal()
        self.assertEqual(inst_rect_diag, self.ctrl_rect_diag)
        self.assertEqual(inst_sqr_diag, self.ctrl_sqr_diag)

    def test_get_radius_of_circumscribed_circle(self):
        result_rect = self.normal_rect.get_radius_of_circumscribed_circle()
        result_sqr = self.sqr.get_radius_of_circumscribed_circle()
        self.assertEqual(result_rect, self.ctrl_rect_diag/2)
        self.assertEqual(result_sqr, self.ctrl_sqr_diag/2)

    def test_get_radius_of_inscribed_circle(self):
        sqr_radius_of_inscr_circ = self.ctrl_sqr_diag / (math.sqrt(2) * 2)
        self.assertRaises(ValueError, self.normal_rect.get_radius_of_inscribed_circle)
        self.assertEqual(self.sqr.get_radius_of_inscribed_circle(),
                         sqr_radius_of_inscr_circ)


if __name__ == '__main__':
    unittest.main(verbosity=2)
