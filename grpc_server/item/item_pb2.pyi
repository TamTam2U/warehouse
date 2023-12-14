from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("id", "name", "kategoriId")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KATEGORIID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    kategoriId: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., kategoriId: _Optional[str] = ...) -> None: ...

class ItemListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ItemListResponse(_message.Message):
    __slots__ = ("Item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    Item: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, Item: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class ItemDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ItemDetailResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class ItemCreateRequest(_message.Message):
    __slots__ = ("name", "kategoriId")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KATEGORIID_FIELD_NUMBER: _ClassVar[int]
    name: str
    kategoriId: str
    def __init__(self, name: _Optional[str] = ..., kategoriId: _Optional[str] = ...) -> None: ...

class ItemCreateResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class ItemUpdateRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ItemUpdateResponse(_message.Message):
    __slots__ = ("item", "message")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    item: Item
    message: str
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class ItemDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ItemDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
