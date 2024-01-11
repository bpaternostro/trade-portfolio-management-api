from abc import ABC
from abc import abstractmethod

class Exchange(ABC):

    @abstractmethod
    def _connect():
        pass

    @abstractmethod
    def get_rates():
        pass