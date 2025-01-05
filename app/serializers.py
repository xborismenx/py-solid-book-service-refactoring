from __future__ import annotations

import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self):
        pass


class BookJSONSerializer(BookSerializer):
    def __init__(self, book):
        self.title = book.title
        self.content = book.content

    def serialize(self):
        return json.dumps({"title": self.title, "content": self.content})


class BookXMLSerializer(BookSerializer):
    def __init__(self, book):
        self.title = book.title
        self.content = book.content

    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")

class BookSerializer:
    @staticmethod
    def serializer(book, type_serializer: str) -> None | str:
        if type_serializer == "json":
            return BookJSONSerializer(book).serialize()
        elif type_serializer == "xml":
            return BookXMLSerializer(book).serialize()
