# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: barangmasuk.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x62\x61rangmasuk.proto\x12\x0b\x62\x61rangmasuk\"^\n\x0b\x42\x61rangMasuk\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ctanggalMasuk\x18\x03 \x01(\t\x12\x12\n\nsupplierId\x18\x04 \x01(\t\x12\x0b\n\x03qty\x18\x05 \x01(\x05\"\x18\n\x16\x42\x61rangMasukListRequest\"H\n\x17\x42\x61rangMasukListResponse\x12-\n\x0b\x62\x61rangmasuk\x18\x01 \x03(\x0b\x32\x18.barangmasuk.BarangMasuk\"&\n\x18\x42\x61rangMasukDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"J\n\x19\x42\x61rangMasukDetailResponse\x12-\n\x0b\x62\x61rangmasuk\x18\x01 \x01(\x0b\x32\x18.barangmasuk.BarangMasuk\"_\n\x18\x42\x61rangMasukCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0ctanggalMasuk\x18\x02 \x01(\t\x12\x12\n\nsupplierId\x18\x03 \x01(\t\x12\x0b\n\x03qty\x18\x04 \x01(\x05\"J\n\x19\x42\x61rangMasukCreateResponse\x12-\n\x0b\x62\x61rangmasuk\x18\x01 \x01(\x0b\x32\x18.barangmasuk.BarangMasuk\"k\n\x18\x42\x61rangMasukUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ctanggalMasuk\x18\x03 \x01(\t\x12\x12\n\nsupplierId\x18\x04 \x01(\t\x12\x0b\n\x03qty\x18\x05 \x01(\x05\"[\n\x19\x42\x61rangMasukUpdateResponse\x12-\n\x0b\x62\x61rangmasuk\x18\x01 \x01(\x0b\x32\x18.barangmasuk.BarangMasuk\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\x18\x42\x61rangMasukDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\",\n\x19\x42\x61rangMasukDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc8\x03\n\x12\x42\x61rangMasukService\x12Q\n\x04list\x12#.barangmasuk.BarangMasukListRequest\x1a$.barangmasuk.BarangMasukListResponse\x12T\n\x03get\x12%.barangmasuk.BarangMasukDetailRequest\x1a&.barangmasuk.BarangMasukDetailResponse\x12W\n\x06\x63reate\x12%.barangmasuk.BarangMasukCreateRequest\x1a&.barangmasuk.BarangMasukCreateResponse\x12W\n\x06update\x12%.barangmasuk.BarangMasukUpdateRequest\x1a&.barangmasuk.BarangMasukUpdateResponse\x12W\n\x06\x64\x65lete\x12%.barangmasuk.BarangMasukDeleteRequest\x1a&.barangmasuk.BarangMasukDeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'barangmasuk_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BARANGMASUK']._serialized_start=34
  _globals['_BARANGMASUK']._serialized_end=128
  _globals['_BARANGMASUKLISTREQUEST']._serialized_start=130
  _globals['_BARANGMASUKLISTREQUEST']._serialized_end=154
  _globals['_BARANGMASUKLISTRESPONSE']._serialized_start=156
  _globals['_BARANGMASUKLISTRESPONSE']._serialized_end=228
  _globals['_BARANGMASUKDETAILREQUEST']._serialized_start=230
  _globals['_BARANGMASUKDETAILREQUEST']._serialized_end=268
  _globals['_BARANGMASUKDETAILRESPONSE']._serialized_start=270
  _globals['_BARANGMASUKDETAILRESPONSE']._serialized_end=344
  _globals['_BARANGMASUKCREATEREQUEST']._serialized_start=346
  _globals['_BARANGMASUKCREATEREQUEST']._serialized_end=441
  _globals['_BARANGMASUKCREATERESPONSE']._serialized_start=443
  _globals['_BARANGMASUKCREATERESPONSE']._serialized_end=517
  _globals['_BARANGMASUKUPDATEREQUEST']._serialized_start=519
  _globals['_BARANGMASUKUPDATEREQUEST']._serialized_end=626
  _globals['_BARANGMASUKUPDATERESPONSE']._serialized_start=628
  _globals['_BARANGMASUKUPDATERESPONSE']._serialized_end=719
  _globals['_BARANGMASUKDELETEREQUEST']._serialized_start=721
  _globals['_BARANGMASUKDELETEREQUEST']._serialized_end=759
  _globals['_BARANGMASUKDELETERESPONSE']._serialized_start=761
  _globals['_BARANGMASUKDELETERESPONSE']._serialized_end=805
  _globals['_BARANGMASUKSERVICE']._serialized_start=808
  _globals['_BARANGMASUKSERVICE']._serialized_end=1264
# @@protoc_insertion_point(module_scope)
