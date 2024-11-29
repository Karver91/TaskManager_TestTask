from config import settings
from lexicon import ru, en


class LexiconManager:
    @staticmethod
    def get_ru_lexicon():
        return ru._COMMANDS_LEXICON, ru._MESSAGE_LEXICON, ru._EXCEPTION_LEXICON

    @staticmethod
    def get_en_lexicon():
        return en._COMMANDS_LEXICON, en._MESSAGE_LEXICON, en._EXCEPTION_LEXICON


__lm = LexiconManager()

__lang_code = {
    'ru': __lm.get_ru_lexicon,
    'en': __lm.get_en_lexicon
}


def __validate_language(lang):
    if not lang in __lang_code:
        raise ValueError('Такой язык не найден')


def __get_lexicon():
    lang = settings.LANGUAGE
    __validate_language(lang)
    return __lang_code[lang]()


COMMANDS_LEXICON, MESSAGE_LEXICON, EXCEPTION_LEXICON = __get_lexicon()
