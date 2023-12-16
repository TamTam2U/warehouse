from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BarangKeluar(_message.Message):
    __slots__ = ("id", "item", "tanggalKeluar", "supplierID", "qty")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALKELUAR_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    id: int
    item: str
    tanggalKeluar: str
    supplierID: str
    qty: int
    def __init__(self, id: _Optional[int] = ..., item: _Optional[str] = ..., tanggalKeluar: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangKeluarListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BarangKeluarListResponse(_message.Message):
    __slots__ = ("barangkeluar",)
    BARANGKELUAR_FIELD_NUMBER: _ClassVar[int]
    barangkeluar: _containers.RepeatedCompositeFieldContainer[BarangKeluar]
    def __init__(self, barangkeluar: _Optional[_Iterable[_Union[BarangKeluar, _Mapping]]] = ...) -> None: ...

class BarangKeluarDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BarangKeluarDetailResponse(_message.Message):
    __slots__ = ("barangkeluar",)
    BARANGKELUAR_FIELD_NUMBER: _ClassVar[int]
    barangkeluar: BarangKeluar
    def __init__(self, barangkeluar: _Optional[_Union[BarangKeluar, _Mapping]] = ...) -> None: ...

class BarangKeluarCreateRequest(_message.Message):
    __slots__ = ("item", "tanggalKeluar", "supplierID", "qty")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALKELUAR_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    item: str
    tanggalKeluar: str
    supplierID: str
    qty: int
    def __init__(self, item: _Optional[str] = ..., tanggalKeluar: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangKeluarCreateResponse(_message.Message):
    __slots__ = ("barangkeluar",)
    BARANGKELUAR_FIELD_NUMBER: _ClassVar[int]
    barangkeluar: BarangKeluar
    def __init__(self, barangkeluar: _Optional[_Union[BarangKeluar, _Mapping]] = ...) -> None: ...

class BarangKeluarUpdateRequest(_message.Message):
    __slots__ = ("id", "item", "tanggalKeluar", "supplierID", "qty")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TANGGALKELUAR_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    id: int
    item: str
    tanggalKeluar: str
    supplierID: str
    qty: int
    def __init__(self, id: _Optional[int] = ..., item: _Optional[str] = ..., tanggalKeluar: _Optional[str] = ..., supplierID: _Optional[str] = ..., qty: _Optional[int] = ...) -> None: ...

class BarangKeluarUpdateResponse(_message.Message):
    __slots__ = ("barangkeluar", "message")
    BARANGKELUAR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    barangkeluar: BarangKeluar
    message: str
    def __init__(self, barangkeluar: _Optional[_Union[BarangKeluar, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class BarangKeluarDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BarangKeluarDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
