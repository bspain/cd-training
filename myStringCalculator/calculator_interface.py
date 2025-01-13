from abc import ABC, abstractmethod

class CalculatorInterface(ABC):
    @abstractmethod
    def add(self, input: str) -> int:
        pass
    
    @abstractmethod
    def getLastValues(self) -> list[str]:
        pass
