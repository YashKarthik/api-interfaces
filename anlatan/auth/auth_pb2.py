# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='anlatan',
  syntax='proto3',
  serialized_options=b'Z\007./;auth',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nauth.proto\x12\x07\x61nlatan\"$\n\x07Message\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x42\t\n\x07message\"A\n\x08Response\x12\x12\n\nauthorized\x18\x01 \x01(\x08\x12!\n\x07message\x18\x02 \x01(\x0b\x32\x10.anlatan.Message\"U\n\x07Request\x12\x1a\n\rstatic_bearer\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x61uth0\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_static_bearerB\x08\n\x06_auth02B\n\x0b\x41uthService\x12\x33\n\x0c\x41uthenticate\x12\x10.anlatan.Request\x1a\x11.anlatan.ResponseB\tZ\x07./;authb\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='anlatan.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='anlatan.Message.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='anlatan.Message.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=23,
  serialized_end=59,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='anlatan.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorized', full_name='anlatan.Response.authorized', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='anlatan.Response.message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=126,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='anlatan.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='static_bearer', full_name='anlatan.Request.static_bearer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth0', full_name='anlatan.Request.auth0', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_static_bearer', full_name='anlatan.Request._static_bearer',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_auth0', full_name='anlatan.Request._auth0',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=128,
  serialized_end=213,
)

_MESSAGE.oneofs_by_name['message'].fields.append(
  _MESSAGE.fields_by_name['text'])
_MESSAGE.fields_by_name['text'].containing_oneof = _MESSAGE.oneofs_by_name['message']
_RESPONSE.fields_by_name['message'].message_type = _MESSAGE
_REQUEST.oneofs_by_name['_static_bearer'].fields.append(
  _REQUEST.fields_by_name['static_bearer'])
_REQUEST.fields_by_name['static_bearer'].containing_oneof = _REQUEST.oneofs_by_name['_static_bearer']
_REQUEST.oneofs_by_name['_auth0'].fields.append(
  _REQUEST.fields_by_name['auth0'])
_REQUEST.fields_by_name['auth0'].containing_oneof = _REQUEST.oneofs_by_name['_auth0']
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:anlatan.Message)
  })
_sym_db.RegisterMessage(Message)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:anlatan.Response)
  })
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:anlatan.Request)
  })
_sym_db.RegisterMessage(Request)


DESCRIPTOR._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='anlatan.AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=215,
  serialized_end=281,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='anlatan.AuthService.Authenticate',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)
