from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Admin(_message.Message):
    __slots__ = ("id", "email", "password", "otp", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    OTP_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: int
    email: str
    password: str
    otp: str
    token: str
    def __init__(self, id: _Optional[int] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., otp: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class AdminListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminListResponse(_message.Message):
    __slots__ = ("admin",)
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: _containers.RepeatedCompositeFieldContainer[Admin]
    def __init__(self, admin: _Optional[_Iterable[_Union[Admin, _Mapping]]] = ...) -> None: ...

class AdminRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AdminResponse(_message.Message):
    __slots__ = ("admin",)
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: Admin
    def __init__(self, admin: _Optional[_Union[Admin, _Mapping]] = ...) -> None: ...

class AdminCreateRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminCreateResponse(_message.Message):
    __slots__ = ("admin",)
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: Admin
    def __init__(self, admin: _Optional[_Union[Admin, _Mapping]] = ...) -> None: ...

class AdminUpdateRequest(_message.Message):
    __slots__ = ("id", "password")
    ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: int
    password: str
    def __init__(self, id: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class AdminUpdateResponse(_message.Message):
    __slots__ = ("admin",)
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: Admin
    def __init__(self, admin: _Optional[_Union[Admin, _Mapping]] = ...) -> None: ...

class AdminDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AdminDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AdminLoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminLoginResponse(_message.Message):
    __slots__ = ("token", "email", "id")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    email: str
    id: str
    def __init__(self, token: _Optional[str] = ..., email: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AdminLogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AdminLogoutResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AdminOtpRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class AdminOtpResponse(_message.Message):
    __slots__ = ("otp", "email", "message", "id")
    OTP_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    otp: str
    email: str
    message: str
    id: str
    def __init__(self, otp: _Optional[str] = ..., email: _Optional[str] = ..., message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AdminVerifyOtpRequest(_message.Message):
    __slots__ = ("email", "otp")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    OTP_FIELD_NUMBER: _ClassVar[int]
    email: str
    otp: str
    def __init__(self, email: _Optional[str] = ..., otp: _Optional[str] = ...) -> None: ...

class AdminVerifyOtpResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AdminResetPasswordRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminResetPasswordResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
