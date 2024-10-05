import can
from can import Message

class CANMessage(Message):
    data_: list[int]
    id_: int

    def __init__(msg: Message):
        data_ = []
        id_ = 0
        pass
