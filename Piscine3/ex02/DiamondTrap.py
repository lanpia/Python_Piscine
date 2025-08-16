from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """King 클래스: Baratheon과 Lannister를 상속"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    def set_eyes(self, eyes):
        self.eyes = eyes
    def set_hairs(self, hairs):
        self.hairs = hairs
    def get_eyes(self):
        return self.eyes
    def get_hairs(self):
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)