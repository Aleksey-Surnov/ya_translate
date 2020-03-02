import unittest
from ya_translator import Translator, ts, run_translate


class TestNameTranslate(unittest.TestCase):
    """Тест для класса Translator."""

    def setUp(self):
        self.ts = Translator(word='')


    def test_store_memory(self):
        """Проверка сохранения слова или фразы в списке."""
        self.ts.store_memory('привет мой друг')
        self.assertIn('привет мой друг', self.ts.memory)


    def test_correct_translate(self):
        """Проверка правильности перевода простых фраз и слов."""
        format_trans=self.ts.translate_me("привет мой друг")
        self.assertEqual(format_trans.lower(), 'hi my friend')


class TestNameProgramm(unittest.TestCase):
    """Тест для программы ya_translator."""

    def test_run_translate(self):
        """Проверка правильности перевода и вывода списка слов."""
        list_trans = run_translate(['привет мой друг', 'художник', 'женщина'])
        self.assertEqual(list_trans, ['hi my friend', 'artist', 'woman'])


if __name__=='__main__':

    unittest.main()             # запуск теста.


