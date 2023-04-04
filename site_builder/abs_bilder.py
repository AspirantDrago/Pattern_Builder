from abc import ABC, abstractmethod
from typing import Optional, Callable, Any, Iterable
from .site import AbstractSite


class SiteBuilderError(Exception):
    pass


class NotSiteError(SiteBuilderError):
    pass


class AbstractBuilder(ABC):
    def __init__(self):
        self._site: Optional[AbstractSite] = None

    @staticmethod
    def has_site(function: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> Any:
            if self._site is None:
                raise NotSiteError
            return function(self, *args, **kwargs)

        return wrapper

    @abstractmethod
    def create_site(self, name: str) -> None:
        pass

    @has_site
    def get_site(self) -> AbstractSite:
        result = self._site
        self._site = None
        return result

    @abstractmethod
    @has_site
    def add_header(self, text: str, size: int = 1) -> None:
        pass

    @abstractmethod
    @has_site
    def add_paragraph(self, text: str) -> None:
        pass

    @abstractmethod
    @has_site
    def add_text(self, text: str) -> None:
        pass

    @abstractmethod
    @has_site
    def add_bold_text(self, text: str) -> None:
        pass

    @abstractmethod
    @has_site
    def add_italic_text(self, text: str) -> None:
        pass

    @abstractmethod
    @has_site
    def add_bold_italic_text(self, text: str) -> None:
        pass

    @abstractmethod
    @has_site
    def add_list_numerated(self, items: Iterable[str]) -> None:
        pass

    @abstractmethod
    @has_site
    def add_list_marked(self, items: Iterable[str]) -> None:
        pass

    @abstractmethod
    @has_site
    def add_item_of_list(self, text: str) -> None:
        pass