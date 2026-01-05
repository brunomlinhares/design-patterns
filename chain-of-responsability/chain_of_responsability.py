from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
## Exemplo de implementação concreta
## Um sistema de coleta e separação de descartes, contendo lixos orgânicos, recicláveis , químicos , médicos, etc.

## Classe de herança abstrata para os manipuladores

@dataclass
class DiscardObject:
    type: str

class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None):
        self._successor = successor

    def set_successor(self, successor: 'Handler'):
        self._successor = successor

    def handle(self, request: DiscardObject):
        result = self.process(request)
        if result is None and self._successor:
            return self._successor.handle(request)
        return result

    @abstractmethod
    def process(self, request: DiscardObject):
        ...

class OrganicHandler(Handler):
    def process(self, request: DiscardObject):
        if request.type == "organic":
            return "Processed organic waste"
        return None

class RecyclableHandler(Handler):
    def process(self, request: DiscardObject):
        if request.type == "recyclable":
            return "Processed recyclable waste"
        return None

class ChemicalHandler(Handler):
    def process(self, request: DiscardObject):
        if request.type == "chemical":
            return "Processed chemical waste"
        return None

class MedicalHandler(Handler):
    def process(self, request: DiscardObject):
        if request.type == "medical":
            return "Processed medical waste"
        return None
        
class DefaultHandler(Handler):
    def process(self, request: DiscardObject):
        return "Waste type '{}' not recognized, sent to general landfill".format(request.type)
if __name__ == "__main__":
    OBJECTS = [
        DiscardObject("organic"),
        DiscardObject("recyclable"),
        DiscardObject("chemical"),
        DiscardObject("medical"),
        DiscardObject("unknown"),
    ]
    # Configuração da cadeia de responsabilidade
    organic_handler = OrganicHandler()
    recyclable_handler = RecyclableHandler()
    chemical_handler = ChemicalHandler()        
    medical_handler = MedicalHandler()
    default_handler = DefaultHandler()

    # Organização da cadeia
    organic_handler.set_successor(recyclable_handler)
    recyclable_handler.set_successor(chemical_handler)
    chemical_handler.set_successor(medical_handler)
    medical_handler.set_successor(default_handler)

    # Processamento dos objetos
    for obj in OBJECTS:
        result = organic_handler.handle(obj)
        print(f"Object type: {obj.type} - {result}")
