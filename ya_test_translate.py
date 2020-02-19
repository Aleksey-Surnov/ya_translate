import unittest
from ya_translate import Translate, ts, run_translate


class NameTestTranslate(unittest.TestCase):
    """"Тест для класса Translate"""

    def setUp(self):
        self.ts = Translate(word='')


    def test_store_memory(self):
        """"Проверка сохранения слова или фразы в списке"""
        self.ts.store_memory('привет мой друг')
        self.assertIn('привет мой друг', self.ts.memory)


    def test_correct_translate(self):
        """"Проверка правильности перевода простых фраз и слов"""
        format_trans=self.ts.translate_me("привет мой друг")
        self.assertEqual(format_trans.lower(), 'hi my friend')


class NameTestProgramm(unittest.TestCase):
    """"Тест для программы ya_translate"""

    def test_run_translate(self):
        """"Проверка правильности перевода и вывода списка слов"""
        list_trans = run_translate(['привет мой друг', 'художник', 'женщина'])
        self.assertEqual(list_trans, ['hi my friend', 'artist', 'woman'])


if __name__=='__main__':

    unittest.main()             # запуск теста


