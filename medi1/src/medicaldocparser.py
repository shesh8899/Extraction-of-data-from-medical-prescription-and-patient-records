from abc import ABC, abstractmethod
class medical_doc_parser(ABC):
    def __init__(self,text):
        self.text=text

    @abstractmethod
    def parse(self):
        pass