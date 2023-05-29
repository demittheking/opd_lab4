import unittest
from convert import app


class TestConversion(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_checkRightIndex(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_checkNotRightIndex(self):
        result=self.app.get('/')
        self.assertEqual(result.status_code,300)

    def test_rightConversion(self):
        data = {'currency_from': 'CHF', 'currency_to': 'GBP', 'amount': '30'}
        result = self.app.post('/convert', data=data)
        self.assertIn(b'<p>30.0 CHF = 26.83 GBP</p>', result.data)

    def test_rightConversionWithIndex(self):
        data = {'currency_from': 'USD', 'currency_to': 'EUR', 'amount': '2'}
        result = self.app.post('/convert', data=data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<p>2.0 USD = 1.86 EUR</p>', result.data)

    def test_notRightConversion(self):
        data = {'currency_from': 'unknown_valuta', 'currency_to': 'EUR', 'amount': '10'}
        result = self.app.post('/convert', data=data)
        self.assertEqual(result.status_code, 400)


if __name__ == '__main__':
    unittest.main()