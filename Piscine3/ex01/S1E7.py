from abc import ABC, abstractmethod
from S1E9 import Character, Stark


class Lannister(Character):
    """Lannister 클래스"""
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """is_alive를 False로 변경"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Lannister 가문을 생성하는 메서드"""
        return cls(first_name, is_alive)

    def __str__(self):
        '''docstring'''
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self):
        """Returns a string representation of the object."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """is_alive를 False로 변경"""
        self.is_alive = False
    
    def __str__(self):
        '''docstring'''
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self):
        """Returns a string representation of the object."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
