from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass


class SimpleMessage(Message):
    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content


class MessageDecorator(Message):
    def __init__(self, message: Message):
        self._message = message

    def get_content(self) -> str:
        return self._message.get_content()


class EncryptedMessage(MessageDecorator):
    def get_content(self) -> str:
        return f"Encrypted({super().get_content()})"

class HTMLMessage(MessageDecorator):
    def get_content(self) -> str:
        return f"<html>{super().get_content()}</html>"


# Original message
simple_message = SimpleMessage("Hello, World!")

# Encrypted message
encrypted_message = EncryptedMessage(simple_message)
print(encrypted_message.get_content())

# HTML message
html_message = HTMLMessage(simple_message)
print(html_message.get_content())  # Output: <html>Hello, World!</html

# Encrypted and HTML message
encrypted_html_message = HTMLMessage(encrypted_message)
print(encrypted_html_message.get_content())
