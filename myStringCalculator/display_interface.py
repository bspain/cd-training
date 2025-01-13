from abc import ABC, abstractmethod

class DisplayInterface(ABC):
    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_display(self):
        pass