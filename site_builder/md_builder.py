from typing import Iterable

from .abs_bilder import AbstractBuilder
from .md_site import MarkDownSite


class MarkDownBuilder(AbstractBuilder):
    """
    Класс MarkDownBuilder предназначен для создания текстовых документов.
    MarkDownBuilder унаследован от класса AbstractBuilder.
    Создает файл формата .md (MarkDown).
    """

    def create_site(self, name: str) -> None:
        """
        Функция по созданию сайта
        :param name: str
        :return: None
        """
        self._site = MarkDownSite(filename=name)

    @AbstractBuilder.has_site
    def add_header(self, text: str, size: int = 1) -> None:
        """
        Функция по созданию заголовка.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :param size: int (По умолчанию = 1)
        :return: None
        """
        if size < 1 or size > 6:
            raise ValueError('Headers can be 1-6 size')
        self._site.write_line('#' * size + ' ' + text)

    @AbstractBuilder.has_site
    def add_paragraph(self, text: str) -> None:
        """
        Функция по добавлению параграфа.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        self._site.write('\n\n' + text)

    @AbstractBuilder.has_site
    def add_text(self, text: str) -> None:
        """
        Функция по добавлению текста.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        self._site.write_line(text)

    @AbstractBuilder.has_site
    def add_bold_text(self, text: str) -> None:
        """
        Функция по добавлению текста жирным шрифтом.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        self._site.write_line(f'**{text}**')

    @AbstractBuilder.has_site
    def add_italic_text(self, text: str) -> None:
        """
        Функция по добавлению текста курсивом.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        self._site.write_line(f'*{text}*')

    @AbstractBuilder.has_site
    def add_bold_italic_text(self, text: str) -> None:
        """
        Функция по добавлению текста курсивом и жирным шрифтом.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        self._site.write_line(f'***{text}***')

    @AbstractBuilder.has_site
    def add_list_numerated(self, items: Iterable[str]) -> None:
        """
        Функция по добавлению нумерации страницы.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param items: Iterable[str]
        :return: None
        """
        self._site.write_line()
        for i, item in enumerate(items, 1):
            self._site.write_line(f'{i}. {item}')
        self._site.write_line()

    @AbstractBuilder.has_site
    def add_list_marked(self, items: Iterable[str]) -> None:
        """
        Функция по добавлению маркированного текста.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param items: Iterable[str]
        :return: None
        """
        self._site.write_line('<ul>')
        for item in items:
            self._site.write_line(f'- {item}')
        self._site.write_line('</ul>')

    @AbstractBuilder.has_site
    def add_item_of_list(self, text: str) -> None:
        """
        Функция по добавлению элемента на страницу.
        Для этой функции используется декоратор @AbstractBuilder.has_site.
        :param text: str
        :return: None
        """
        pass