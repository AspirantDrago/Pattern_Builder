from webbrowser import open as open_url

from .site import AbstractSite


class HTMLSite(AbstractSite):
    def save(self):
        filename = self._filename + '.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self._content)
        open_url(filename)
