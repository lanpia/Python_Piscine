from abc import ABC, abstractmethod

class Character(ABC):
    """추상 클래스: Character
    속성:
      - first_name: 캐릭터 이름
      - is_alive: 생존 상태 (기본값: True)"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """생성자 메서드"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """캐릭터를 죽이는 추상 메서드"""
        pass

class Stark(Character):
    """Stark 클래스: Character를 상속"""
    def die(self):
        """is_alive를 False로 변경"""
        self.is_alive = False
