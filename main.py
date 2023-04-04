from site_builder import HTMLBuilder, MarkDownBuilder, AbstractBuilder


class Director:
    def __init__(self, builder: AbstractBuilder):
        self._bulder = builder

    def make_google(self) -> None:
        self._bulder.create_site('google')

        self._bulder.add_header('Google')
        self._bulder.add_header('Найдётся всё', size=2)
        self._bulder.add_italic_text('(ну почти всё. Товарищ майор всё-таки следит)')
        self._bulder.add_paragraph('')
        self._bulder.add_bold_text('НИЧЕГО НЕ НАЙДЕНО')
        self._bulder.add_paragraph('А именно:')
        self._bulder.add_list_numerated([
            'Как приготовить безе из питона',
            'Как повестить картину на плюсах',
            'Как выстрелить себе в ногу'
        ])
        site = self._bulder.get_site()
        site.save()


director1 = Director(HTMLBuilder())
director1.make_google()
