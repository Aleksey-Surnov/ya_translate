import unittest
from yandex_translate import translate_me

class NameTestCase(unittest.TestCase):
    """"Тест для функции translate_me"""

    def test_correct_translate(self):
        """"Проверка правильности перевода простых фраз и слов"""
        format_trans=translate_me("Привет мой друг")
        self.assertEqual(format_trans, 'Hi my friend')

if __name__=="__name__":
    unittest.main()