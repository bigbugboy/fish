import enum
import time

from tortoise.models import Model
from tortoise import fields


class SingleChoice(Model):

    class LevelType(enum.IntEnum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    id = fields.IntField(pk=True)
    level = fields.IntEnumField(LevelType)
    question = fields.CharField(max_length=1000)
    choice_a = fields.CharField(max_length=256)
    choice_b = fields.CharField(max_length=256)
    choice_c = fields.CharField(max_length=256)
    choice_d = fields.CharField(max_length=256)
    choice_right = fields.CharField(max_length=1)
    desc = fields.TextField()
    created_at = fields.IntField(default=time.time)
    updated_at = fields.IntField(default=time.time)
    status = fields.SmallIntField(default=1)

    def __str__(self):
        return str(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "level": self.level.name,
            "question": self.question,
            "choice_a": self.choice_a,
            "desc": self.desc,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
