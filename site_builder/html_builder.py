from typing import Iterable

from .abs_bilder import AbstractBuilder
from .html_site import HTMLSite
from .site import AbstractSite


class HTMLBuilder(AbstractBuilder):
    """Класс для создания и заполнения HTML сайта"""
    def create_site(self, name: str) -> None:
        """
            Метод который создает HTML файл с базовой разметкой
            :param name: Название html файла
            :type name: str
        """
        self._site = HTMLSite(filename=name)
        self._site.write_line(
            f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{name}</title>
            </head>
            <body>'''
        )

    @AbstractBuilder.has_site
    def get_site(self) -> AbstractSite:
        """ 'Закрывает вверску сайта' и возвращает html файл """
        self._site.write("</body>\n</html>")
        return super().get_site()

    @AbstractBuilder.has_site
    def add_header(self, text: str, size: int = 1) -> None:
        """
            Метод который добавляет загаловок 1-6 уровня (<h{size}>)
            :param text: текст заголовка
            :type text: str
            :param size: уровень заголовка
            :type size: int

        """
        if size < 1 or size > 6:
            raise ValueError('Headers can be 1-6 size')
        self._site.write_line(f'<h{size}>{text}</h{size}>')

    @AbstractBuilder.has_site
    def add_paragraph(self, text: str) -> None:
        """
            Добавляет в верстку параграф  (<p>)
            :param text: Текст параграфа
            :type text: str
        """
        self._site.write_line(f'<p>{text}</p>')

    @AbstractBuilder.has_site
    def add_text(self, text: str) -> None:
        """
            Добавляет в верстку текст (<span>)
            :param text: текст
            :type text: str
        """
        self._site.write(f'<span>{text}</span>')

    @AbstractBuilder.has_site
    def add_bold_text(self, text: str) -> None:
        """
            Добавляет в верстку жирный текст (<b>)
            :param text: текст
            :type text: str
        """
        self._site.write(f'<b>{text}</b>')

    @AbstractBuilder.has_site
    def add_italic_text(self, text: str) -> None:
        """
            Добавляет в верстку курсивный текст (<i>)
            :param text: текст
            :type text: str
        """
        self._site.write(f'<i>{text}</i>')

    @AbstractBuilder.has_site
    def add_bold_italic_text(self, text: str) -> None:
        """
            Добавляет в верстку жирный курсивный текст (<b> <i>)
            :param text: текст
            :type text: str
        """
        self._site.write(f'<b><i>{text}</i></b>')

    @AbstractBuilder.has_site
    def add_list_numerated(self, items: Iterable[str]) -> None:
        """
            Добавляет нумеровнанный спискок (<ol>)
            :param items: список элементов
            :type items: Iterable
        """
        self._site.write_line('<ol>')
        for item in items:
            self.add_item_of_list(item)
        self._site.write_line('</ol>')

    @AbstractBuilder.has_site
    def add_list_marked(self, items: Iterable[str]) -> None:
        """
            Добавляет маркерованный спискок (<ul>)
            :param items: список элементов
            :type items: Iterable
        """
        self._site.write_line('<ul>')
        for item in items:
            self.add_item_of_list(item)
        self._site.write_line('</ul>')

    @AbstractBuilder.has_site
    def add_item_of_list(self, text: str) -> None:
        """
            Добавляет элемент списка (<li>)
            :param text: контент элемента
            :type text: str
        """
        self._site.write_line(f'<li>{text}</li>')
