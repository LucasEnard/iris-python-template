from grongier.pex import Message

from dataclasses import dataclass

from obj import CustomObject

@dataclass
class CustomRequest(Message):
    custobj:CustomObject = None

@dataclass
class CustomResponse(Message):
    custobj:CustomObject = None
    custint:int = None