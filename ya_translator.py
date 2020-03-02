from translator import Translator
from colorama import init, Fore, Back
init(convert=True)


"""Программа выполняет перевод слов с русского языка на английский."""
"""Скрипт не чувствителен к регистру."""

ts = Translator(word='')
"""Определим переменную как экземпляр класса."""

def get_tarnslate_word(word=''):
    """Выполнение перевода слова с русского языка на английский."""
    word_trans=ts.translate_me(word)
    return word_trans.lower()


def input_word():
    """Выполнение ввода слов для перевода."""
    while True:
        print(Fore.BLUE+ 'Введите слово для перевода или введите "stop" для остановки и получения результата: ', end='')
        ts.word=input().lower()
        if ts.word=='stop': break
        else:
            ts.store_memory(ts.word)
    return ts.memory


def run_translate(word_list=[]):
    """Переводчик."""
    result_translate=[]
    for word in word_list:
        result_translate.append(get_tarnslate_word(word))
    return result_translate


if __name__=="__main__":

    word_list=(input_word())
    translate_word=run_translate(word_list)
    """Запуск переводчика."""
    for i in range(len(translate_word)):
        """Выводим результат в цвете."""
        print(Fore.GREEN+translate_word[i])








