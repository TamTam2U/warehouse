# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: itemrack.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eitemrack.proto\x12\x08itemrack\"6\n\x08ItemRack\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06itemId\x18\x02 \x01(\x05\x12\x0e\n\x06rackId\x18\x03 \x01(\x05\"\x15\n\x13ItemRackListRequest\"<\n\x14ItemRackListResponse\x12$\n\x08itemRack\x18\x01 \x03(\x0b\x32\x12.itemrack.ItemRack\"#\n\x15ItemRackDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\">\n\x16ItemRackDetailResponse\x12$\n\x08itemRack\x18\x01 \x01(\x0b\x32\x12.itemrack.ItemRack\"7\n\x15ItemRackCreateRequest\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\x0e\n\x06rackId\x18\x02 \x01(\x05\">\n\x16ItemRackCreateResponse\x12$\n\x08itemRack\x18\x01 \x01(\x0b\x32\x12.itemrack.ItemRack\"C\n\x15ItemRackUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06itemId\x18\x02 \x01(\x05\x12\x0e\n\x06rackId\x18\x03 \x01(\x05\">\n\x16ItemRackUpdateResponse\x12$\n\x08itemRack\x18\x01 \x01(\x0b\x32\x12.itemrack.ItemRack\"#\n\x15ItemRackDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x16ItemRackDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\x13ItemByRackIdRequest\x12\x0e\n\x06rackId\x18\x01 \x01(\x05\"<\n\x14ItemByRackIdResponse\x12$\n\x08itemRack\x18\x01 \x03(\x0b\x32\x12.itemrack.ItemRack2\xd8\x03\n\x0fItemRackService\x12\x45\n\x04list\x12\x1d.itemrack.ItemRackListRequest\x1a\x1e.itemrack.ItemRackListResponse\x12H\n\x03get\x12\x1f.itemrack.ItemRackDetailRequest\x1a .itemrack.ItemRackDetailResponse\x12K\n\x06\x63reate\x12\x1f.itemrack.ItemRackCreateRequest\x1a .itemrack.ItemRackCreateResponse\x12K\n\x06update\x12\x1f.itemrack.ItemRackUpdateRequest\x1a .itemrack.ItemRackUpdateResponse\x12K\n\x06\x64\x65lete\x12\x1f.itemrack.ItemRackDeleteRequest\x1a .itemrack.ItemRackDeleteResponse\x12M\n\x0citemByRackId\x12\x1d.itemrack.ItemByRackIdRequest\x1a\x1e.itemrack.ItemByRackIdResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'itemrack_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ITEMRACK']._serialized_start=28
  _globals['_ITEMRACK']._serialized_end=82
  _globals['_ITEMRACKLISTREQUEST']._serialized_start=84
  _globals['_ITEMRACKLISTREQUEST']._serialized_end=105
  _globals['_ITEMRACKLISTRESPONSE']._serialized_start=107
  _globals['_ITEMRACKLISTRESPONSE']._serialized_end=167
  _globals['_ITEMRACKDETAILREQUEST']._serialized_start=169
  _globals['_ITEMRACKDETAILREQUEST']._serialized_end=204
  _globals['_ITEMRACKDETAILRESPONSE']._serialized_start=206
  _globals['_ITEMRACKDETAILRESPONSE']._serialized_end=268
  _globals['_ITEMRACKCREATEREQUEST']._serialized_start=270
  _globals['_ITEMRACKCREATEREQUEST']._serialized_end=325
  _globals['_ITEMRACKCREATERESPONSE']._serialized_start=327
  _globals['_ITEMRACKCREATERESPONSE']._serialized_end=389
  _globals['_ITEMRACKUPDATEREQUEST']._serialized_start=391
  _globals['_ITEMRACKUPDATEREQUEST']._serialized_end=458
  _globals['_ITEMRACKUPDATERESPONSE']._serialized_start=460
  _globals['_ITEMRACKUPDATERESPONSE']._serialized_end=522
  _globals['_ITEMRACKDELETEREQUEST']._serialized_start=524
  _globals['_ITEMRACKDELETEREQUEST']._serialized_end=559
  _globals['_ITEMRACKDELETERESPONSE']._serialized_start=561
  _globals['_ITEMRACKDELETERESPONSE']._serialized_end=602
  _globals['_ITEMBYRACKIDREQUEST']._serialized_start=604
  _globals['_ITEMBYRACKIDREQUEST']._serialized_end=641
  _globals['_ITEMBYRACKIDRESPONSE']._serialized_start=643
  _globals['_ITEMBYRACKIDRESPONSE']._serialized_end=703
  _globals['_ITEMRACKSERVICE']._serialized_start=706
  _globals['_ITEMRACKSERVICE']._serialized_end=1178
# @@protoc_insertion_point(module_scope)
