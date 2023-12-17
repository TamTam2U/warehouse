from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BarangMasuk(_message.Message):
    __slots__ = ("id", "item", "tanggalMasuk", "supplierID", "qty")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALMASUK_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    id: int
    item: str
    tanggalMasuk: str
    supplierID: str
    qty: int
    def __init__(self, id: _Optional[int] = ..., item: _Optional[str] = ..., tanggalMasuk: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangMasukListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BarangMasukListResponse(_message.Message):
    __slots__ = ("barangmasuk",)
    BARANGMASUK_FIELD_NUMBER: _ClassVar[int]
    barangmasuk: _containers.RepeatedCompositeFieldContainer[BarangMasuk]
    def __init__(self, barangmasuk: _Optional[_Iterable[_Union[BarangMasuk, _Mapping]]] = ...) -> None: ...

class BarangMasukDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BarangMasukDetailResponse(_message.Message):
    __slots__ = ("barangmasuk",)
    BARANGMASUK_FIELD_NUMBER: _ClassVar[int]
    barangmasuk: BarangMasuk
    def __init__(self, barangmasuk: _Optional[_Union[BarangMasuk, _Mapping]] = ...) -> None: ...

class BarangMasukCreateRequest(_message.Message):
    __slots__ = ("item", "tanggalMasuk", "supplierID", "qty")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALMASUK_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    item: str
    tanggalMasuk: str
    supplierID: str
    qty: int
    def __init__(self, item: _Optional[str] = ..., tanggalMasuk: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangMasukCreateResponse(_message.Message):
    __slots__ = ("barangmasuk",)
    BARANGMASUK_FIELD_NUMBER: _ClassVar[int]
    barangmasuk: BarangMasuk
    def __init__(self, barangmasuk: _Optional[_Union[BarangMasuk, _Mapping]] = ...) -> None: ...

class BarangMasukUpdateRequest(_message.Message):
    __slots__ = ("id", "item", "tanggalMasuk", "supplierID", "qty")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALMASUK_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    id: int
    item: str
    tanggalMasuk: str
    supplierID: str
    qty: int
    def __init__(self, id: _Optional[int] = ..., item: _Optional[str] = ..., tanggalMasuk: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangMasukUpdateResponse(_message.Message):
    __slots__ = ("barangmasuk", "message")
    BARANGMASUK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    barangmasuk: BarangMasuk
    message: str
    def __init__(self, barangmasuk: _Optional[_Union[BarangMasuk, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class BarangMasukDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BarangMasukDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
