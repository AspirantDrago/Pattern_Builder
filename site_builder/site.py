from abc import ABC, abstractmethod
from typing import Optional


class AbstractSite(ABC):
    def __init__(self, filename: str):
        self._filename = filename
        self._content = ''
        self._new_line = '\n'

    @abstractmethod
    def save(self):
        pass

    def write(self, text: str) -> None:
        self._content += text

    def write_line(self, text: Optional[str] = '') -> None:
        self.write(text + self._new_line)

    def __str__(self) -> str:
        return self._content

    def __len__(self) -> int:
        return len(self._content)