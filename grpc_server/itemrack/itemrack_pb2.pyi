from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemRack(_message.Message):
    __slots__ = ("id", "itemId", "rackId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    RACKID_FIELD_NUMBER: _ClassVar[int]
    id: int
    itemId: int
    rackId: int
    def __init__(self, id: _Optional[int] = ..., itemId: _Optional[int] = ..., rackId: _Optional[int] = ...) -> None: ...

class ItemRackListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ItemRackListResponse(_message.Message):
    __slots__ = ("itemRack",)
    ITEMRACK_FIELD_NUMBER: _ClassVar[int]
    itemRack: _containers.RepeatedCompositeFieldContainer[ItemRack]
    def __init__(self, itemRack: _Optional[_Iterable[_Union[ItemRack, _Mapping]]] = ...) -> None: ...

class ItemRackDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ItemRackDetailResponse(_message.Message):
    __slots__ = ("itemRack",)
    ITEMRACK_FIELD_NUMBER: _ClassVar[int]
    itemRack: ItemRack
    def __init__(self, itemRack: _Optional[_Union[ItemRack, _Mapping]] = ...) -> None: ...

class ItemRackCreateRequest(_message.Message):
    __slots__ = ("itemId", "rackId")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    RACKID_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    rackId: int
    def __init__(self, itemId: _Optional[int] = ..., rackId: _Optional[int] = ...) -> None: ...

class ItemRackCreateResponse(_message.Message):
    __slots__ = ("itemRack",)
    ITEMRACK_FIELD_NUMBER: _ClassVar[int]
    itemRack: ItemRack
    def __init__(self, itemRack: _Optional[_Union[ItemRack, _Mapping]] = ...) -> None: ...

class ItemRackUpdateRequest(_message.Message):
    __slots__ = ("id", "itemId", "rackId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    RACKID_FIELD_NUMBER: _ClassVar[int]
    id: int
    itemId: int
    rackId: int
    def __init__(self, id: _Optional[int] = ..., itemId: _Optional[int] = ..., rackId: _Optional[int] = ...) -> None: ...

class ItemRackUpdateResponse(_message.Message):
    __slots__ = ("itemRack",)
    ITEMRACK_FIELD_NUMBER: _ClassVar[int]
    itemRack: ItemRack
    def __init__(self, itemRack: _Optional[_Union[ItemRack, _Mapping]] = ...) -> None: ...

class ItemRackDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ItemRackDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
