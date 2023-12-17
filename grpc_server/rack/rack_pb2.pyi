from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rack(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class RackListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RackListResponse(_message.Message):
    __slots__ = ("rack",)
    RACK_FIELD_NUMBER: _ClassVar[int]
    rack: _containers.RepeatedCompositeFieldContainer[Rack]
    def __init__(self, rack: _Optional[_Iterable[_Union[Rack, _Mapping]]] = ...) -> None: ...

class RackDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RackDetailResponse(_message.Message):
    __slots__ = ("rack",)
    RACK_FIELD_NUMBER: _ClassVar[int]
    rack: Rack
    def __init__(self, rack: _Optional[_Union[Rack, _Mapping]] = ...) -> None: ...

class RackCreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RackCreateResponse(_message.Message):
    __slots__ = ("rack",)
    RACK_FIELD_NUMBER: _ClassVar[int]
    rack: Rack
    def __init__(self, rack: _Optional[_Union[Rack, _Mapping]] = ...) -> None: ...

class RackUpdateRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class RackUpdateResponse(_message.Message):
    __slots__ = ("rack", "message")
    RACK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    rack: Rack
    message: str
    def __init__(self, rack: _Optional[_Union[Rack, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class RackDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RackDeleteResponse(_message.Message):
    __slots__ = ("rack", "message")
    RACK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    rack: Rack
    message: str
    def __init__(self, rack: _Optional[_Union[Rack, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class ItemRackListRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
