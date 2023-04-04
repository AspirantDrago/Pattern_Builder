from .site import AbstractSite


class MarkDownSite(AbstractSite):
    def save(self):
        filename = self._filename + '.md'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self._content)
