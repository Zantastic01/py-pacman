from monster import *
from field import *

class Rules:
  SHIFT_THRESHOLD = 40
  def get_collision(self, animal, animalType):
    animalInCollision = self.get_collision_in_field(animal.field, animalType)

    if animal.shift >= self.SHIFT_THRESHOLD:
      nextField = animal.next_field()
      if isinstance(nextField, Field):
        animalInCollision = animalInCollision + self.get_collision_in_field(nextField, animalType)
    return animalInCollision

  def get_collision_in_field(self, field, animalType):
    animalInField = self.check_is_animal(field, animalType)
    if isinstance(animalInField, animalType):
      return [animalInField]
    return []

  def check_is_monster(self, field):
    return self.check_is_animal(field, Monster)

  def check_is_pacman(self, field):
    return self.check_is_animal(field, Pacman)

  def check_is_animal(self, field, animalType):
    for animal in field.animals:
      if isinstance(animal, animalType):
        return animal
    return False
