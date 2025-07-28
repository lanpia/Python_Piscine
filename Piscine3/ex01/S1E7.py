from abc import ABC, abstractmethod
from S1E9 import Character, Stark


class Lannister(Character):
    """Lannister 클래스"""
    def die(self):
        """is_alive를 False로 변경"""
        self.is_alive = False

    def pay_debt(self):
        """Lannister 가문의 말을 출력"""
        return "A Lannister always pays his debts"
    def create_lannister(self, other):
        """Lannister 가문을 생성하는 메서드"""
        return Lannister(other.first_name, other.is_alive)

class Baratheon(Character):
    """Baratheon 클래스"""
    def die(self):
        """is_alive를 False로 변경"""
        self.is_alive = False

    def rule(self):
        """Baratheon 가문의 말을 출력"""
        return "The Iron Throne is mine by right"