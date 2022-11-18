# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dashboard.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64\x61shboard.proto\x12\x07gooseai\"\xa9\x01\n\x12OrganizationMember\x12+\n\x0corganization\x18\x01 \x01(\x0b\x32\x15.gooseai.Organization\x12 \n\x04user\x18\x02 \x01(\x0b\x32\r.gooseai.UserH\x00\x88\x01\x01\x12\'\n\x04role\x18\x03 \x01(\x0e\x32\x19.gooseai.OrganizationRole\x12\x12\n\nis_default\x18\x04 \x01(\x08\x42\x07\n\x05_user\"h\n\x11OrganizationGrant\x12\x16\n\x0e\x61mount_granted\x18\x01 \x01(\x01\x12\x13\n\x0b\x61mount_used\x18\x02 \x01(\x01\x12\x12\n\nexpires_at\x18\x03 \x01(\x04\x12\x12\n\ngranted_at\x18\x04 \x01(\x04\"V\n\x17OrganizationPaymentInfo\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x01\x12*\n\x06grants\x18\x02 \x03(\x0b\x32\x1a.gooseai.OrganizationGrant\"I\n\x16OrganizationAutoCharge\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x04\"\xbc\x02\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12,\n\x07members\x18\x04 \x03(\x0b\x32\x1b.gooseai.OrganizationMember\x12;\n\x0cpayment_info\x18\x05 \x01(\x0b\x32 .gooseai.OrganizationPaymentInfoH\x00\x88\x01\x01\x12\x1f\n\x12stripe_customer_id\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x39\n\x0b\x61uto_charge\x18\x07 \x01(\x0b\x32\x1f.gooseai.OrganizationAutoChargeH\x02\x88\x01\x01\x42\x0f\n\r_payment_infoB\x15\n\x13_stripe_customer_idB\x0e\n\x0c_auto_charge\"<\n\x06\x41PIKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tis_secret\x18\x02 \x01(\x08\x12\x12\n\ncreated_at\x18\x03 \x01(\x04\"\xf7\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x07\x61uth_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0fprofile_picture\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x32\n\rorganizations\x18\x05 \x03(\x0b\x32\x1b.gooseai.OrganizationMember\x12!\n\x08\x61pi_keys\x18\x07 \x03(\x0b\x32\x0f.gooseai.APIKey\x12\x12\n\ncreated_at\x18\x08 \x01(\x04\x12\x1b\n\x0e\x65mail_verified\x18\t \x01(\x08H\x01\x88\x01\x01\x42\n\n\x08_auth_idB\x11\n\x0f_email_verified\"9\n\x08\x43ostData\x12\x15\n\ramount_tokens\x18\x01 \x01(\r\x12\x16\n\x0e\x61mount_credits\x18\x02 \x01(\x01\"\xba\x01\n\x0bUsageMetric\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x0e\n\x06\x65ngine\x18\x02 \x01(\t\x12%\n\ninput_cost\x18\x03 \x01(\x0b\x32\x11.gooseai.CostData\x12&\n\x0boutput_cost\x18\x04 \x01(\x0b\x32\x11.gooseai.CostData\x12\x11\n\x04user\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x15\x61ggregation_timestamp\x18\x06 \x01(\x04\x42\x07\n\x05_user\":\n\tCostTotal\x12\x15\n\ramount_tokens\x18\x01 \x01(\r\x12\x16\n\x0e\x61mount_credits\x18\x02 \x01(\x01\"e\n\x10TotalMetricsData\x12\'\n\x0binput_total\x18\x01 \x01(\x0b\x32\x12.gooseai.CostTotal\x12(\n\x0coutput_total\x18\x02 \x01(\x0b\x32\x12.gooseai.CostTotal\"Z\n\x07Metrics\x12%\n\x07metrics\x18\x01 \x03(\x0b\x32\x14.gooseai.UsageMetric\x12(\n\x05total\x18\x02 \x01(\x0b\x32\x19.gooseai.TotalMetricsData\"\x0e\n\x0c\x45mptyRequest\"$\n\x16GetOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x99\x01\n\x11GetMetricsRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nrange_from\x18\x03 \x01(\x04\x12\x10\n\x08range_to\x18\x04 \x01(\x04\x12#\n\x1binclude_per_request_metrics\x18\x05 \x01(\x08\x42\n\n\x08_user_id\"\"\n\rAPIKeyRequest\x12\x11\n\tis_secret\x18\x01 \x01(\x08\"\x1f\n\x11\x41PIKeyFindRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n UpdateDefaultOrganizationRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"\"\n\x0e\x43lientSettings\x12\x10\n\x08settings\x18\x01 \x01(\x0c\"\x80\x01\n\x1d\x43reateAutoChargeIntentRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x17\n\x0fmonthly_maximum\x18\x02 \x01(\x04\x12\x15\n\rminimum_value\x18\x03 \x01(\x04\x12\x16\n\x0e\x61mount_credits\x18\x04 \x01(\x04\">\n\x13\x43reateChargeRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\"R\n\x11GetChargesRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x12\n\nrange_from\x18\x02 \x01(\x04\x12\x10\n\x08range_to\x18\x03 \x01(\x04\"z\n\x06\x43harge\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04paid\x18\x02 \x01(\x08\x12\x14\n\x0creceipt_link\x18\x03 \x01(\t\x12\x14\n\x0cpayment_link\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x04\x12\x16\n\x0e\x61mount_credits\x18\x06 \x01(\x04\"+\n\x07\x43harges\x12 \n\x07\x63harges\x18\x01 \x03(\x0b\x32\x0f.gooseai.Charge\"/\n\x14GetAutoChargeRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"\x90\x01\n\x10\x41utoChargeIntent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cpayment_link\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x04\x12\x17\n\x0fmonthly_maximum\x18\x04 \x01(\x04\x12\x15\n\rminimum_value\x18\x05 \x01(\x04\x12\x16\n\x0e\x61mount_credits\x18\x06 \x01(\x04\"5\n\x15UpdateUserInfoRequest\x12\x12\n\x05\x65mail\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_email\"*\n\x18UserPasswordChangeTicket\x12\x0e\n\x06ticket\x18\x01 \x01(\t\"@\n\x1eListOrganizationMembersRequest\x12\x13\n\x06org_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_org_id\"R\n\x1fRemoveOrganizationMemberRequest\x12\x13\n\x06org_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\tB\t\n\x07_org_id\"\"\n RemoveOrganizationMemberResponse\"x\n\x1c\x41\x64\x64OrganizationMemberRequest\x12\x13\n\x06org_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\'\n\x04role\x18\x03 \x01(\x0e\x32\x19.gooseai.OrganizationRoleB\t\n\x07_org_id\"\x89\x01\n\x1fUpdateOrganizationMemberRequest\x12\x13\n\x06org_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12,\n\x04role\x18\x03 \x01(\x0e\x32\x19.gooseai.OrganizationRoleH\x01\x88\x01\x01\x42\t\n\x07_org_idB\x07\n\x05_role*9\n\x10OrganizationRole\x12\n\n\x06MEMBER\x10\x00\x12\x0e\n\nACCOUNTANT\x10\x01\x12\t\n\x05OWNER\x10\x02\x32\x8b\x0c\n\x10\x44\x61shboardService\x12-\n\x05GetMe\x12\x15.gooseai.EmptyRequest\x1a\r.gooseai.User\x12I\n\x0fGetOrganization\x12\x1f.gooseai.GetOrganizationRequest\x1a\x15.gooseai.Organization\x12:\n\nGetMetrics\x12\x1a.gooseai.GetMetricsRequest\x1a\x10.gooseai.Metrics\x12\x37\n\x0c\x43reateAPIKey\x12\x16.gooseai.APIKeyRequest\x1a\x0f.gooseai.APIKey\x12;\n\x0c\x44\x65leteAPIKey\x12\x1a.gooseai.APIKeyFindRequest\x1a\x0f.gooseai.APIKey\x12U\n\x19UpdateDefaultOrganization\x12).gooseai.UpdateDefaultOrganizationRequest\x1a\r.gooseai.User\x12\x43\n\x11GetClientSettings\x12\x15.gooseai.EmptyRequest\x1a\x17.gooseai.ClientSettings\x12\x45\n\x11SetClientSettings\x12\x17.gooseai.ClientSettings\x1a\x17.gooseai.ClientSettings\x12?\n\x0eUpdateUserInfo\x12\x1e.gooseai.UpdateUserInfoRequest\x1a\r.gooseai.User\x12V\n\x1a\x43reatePasswordChangeTicket\x12\x15.gooseai.EmptyRequest\x1a!.gooseai.UserPasswordChangeTicket\x12\x35\n\rDeleteAccount\x12\x15.gooseai.EmptyRequest\x1a\r.gooseai.User\x12\x61\n\x17ListOrganizationMembers\x12\'.gooseai.ListOrganizationMembersRequest\x1a\x1b.gooseai.OrganizationMember0\x01\x12o\n\x18RemoveOrganizationMember\x12(.gooseai.RemoveOrganizationMemberRequest\x1a).gooseai.RemoveOrganizationMemberResponse\x12[\n\x15\x41\x64\x64OrganizationMember\x12%.gooseai.AddOrganizationMemberRequest\x1a\x1b.gooseai.OrganizationMember\x12\x61\n\x18UpdateOrganizationMember\x12(.gooseai.UpdateOrganizationMemberRequest\x1a\x1b.gooseai.OrganizationMember\x12=\n\x0c\x43reateCharge\x12\x1c.gooseai.CreateChargeRequest\x1a\x0f.gooseai.Charge\x12:\n\nGetCharges\x12\x1a.gooseai.GetChargesRequest\x1a\x10.gooseai.Charges\x12[\n\x16\x43reateAutoChargeIntent\x12&.gooseai.CreateAutoChargeIntentRequest\x1a\x19.gooseai.AutoChargeIntent\x12[\n\x16UpdateAutoChargeIntent\x12&.gooseai.CreateAutoChargeIntentRequest\x1a\x19.gooseai.AutoChargeIntent\x12O\n\x13GetAutoChargeIntent\x12\x1d.gooseai.GetAutoChargeRequest\x1a\x19.gooseai.AutoChargeIntentB\x0eZ\x0c./;dashboardb\x06proto3')

_ORGANIZATIONROLE = DESCRIPTOR.enum_types_by_name['OrganizationRole']
OrganizationRole = enum_type_wrapper.EnumTypeWrapper(_ORGANIZATIONROLE)
MEMBER = 0
ACCOUNTANT = 1
OWNER = 2


_ORGANIZATIONMEMBER = DESCRIPTOR.message_types_by_name['OrganizationMember']
_ORGANIZATIONGRANT = DESCRIPTOR.message_types_by_name['OrganizationGrant']
_ORGANIZATIONPAYMENTINFO = DESCRIPTOR.message_types_by_name['OrganizationPaymentInfo']
_ORGANIZATIONAUTOCHARGE = DESCRIPTOR.message_types_by_name['OrganizationAutoCharge']
_ORGANIZATION = DESCRIPTOR.message_types_by_name['Organization']
_APIKEY = DESCRIPTOR.message_types_by_name['APIKey']
_USER = DESCRIPTOR.message_types_by_name['User']
_COSTDATA = DESCRIPTOR.message_types_by_name['CostData']
_USAGEMETRIC = DESCRIPTOR.message_types_by_name['UsageMetric']
_COSTTOTAL = DESCRIPTOR.message_types_by_name['CostTotal']
_TOTALMETRICSDATA = DESCRIPTOR.message_types_by_name['TotalMetricsData']
_METRICS = DESCRIPTOR.message_types_by_name['Metrics']
_EMPTYREQUEST = DESCRIPTOR.message_types_by_name['EmptyRequest']
_GETORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationRequest']
_GETMETRICSREQUEST = DESCRIPTOR.message_types_by_name['GetMetricsRequest']
_APIKEYREQUEST = DESCRIPTOR.message_types_by_name['APIKeyRequest']
_APIKEYFINDREQUEST = DESCRIPTOR.message_types_by_name['APIKeyFindRequest']
_UPDATEDEFAULTORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateDefaultOrganizationRequest']
_CLIENTSETTINGS = DESCRIPTOR.message_types_by_name['ClientSettings']
_CREATEAUTOCHARGEINTENTREQUEST = DESCRIPTOR.message_types_by_name['CreateAutoChargeIntentRequest']
_CREATECHARGEREQUEST = DESCRIPTOR.message_types_by_name['CreateChargeRequest']
_GETCHARGESREQUEST = DESCRIPTOR.message_types_by_name['GetChargesRequest']
_CHARGE = DESCRIPTOR.message_types_by_name['Charge']
_CHARGES = DESCRIPTOR.message_types_by_name['Charges']
_GETAUTOCHARGEREQUEST = DESCRIPTOR.message_types_by_name['GetAutoChargeRequest']
_AUTOCHARGEINTENT = DESCRIPTOR.message_types_by_name['AutoChargeIntent']
_UPDATEUSERINFOREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserInfoRequest']
_USERPASSWORDCHANGETICKET = DESCRIPTOR.message_types_by_name['UserPasswordChangeTicket']
_LISTORGANIZATIONMEMBERSREQUEST = DESCRIPTOR.message_types_by_name['ListOrganizationMembersRequest']
_REMOVEORGANIZATIONMEMBERREQUEST = DESCRIPTOR.message_types_by_name['RemoveOrganizationMemberRequest']
_REMOVEORGANIZATIONMEMBERRESPONSE = DESCRIPTOR.message_types_by_name['RemoveOrganizationMemberResponse']
_ADDORGANIZATIONMEMBERREQUEST = DESCRIPTOR.message_types_by_name['AddOrganizationMemberRequest']
_UPDATEORGANIZATIONMEMBERREQUEST = DESCRIPTOR.message_types_by_name['UpdateOrganizationMemberRequest']
OrganizationMember = _reflection.GeneratedProtocolMessageType('OrganizationMember', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONMEMBER,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OrganizationMember)
  })
_sym_db.RegisterMessage(OrganizationMember)

OrganizationGrant = _reflection.GeneratedProtocolMessageType('OrganizationGrant', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONGRANT,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OrganizationGrant)
  })
_sym_db.RegisterMessage(OrganizationGrant)

OrganizationPaymentInfo = _reflection.GeneratedProtocolMessageType('OrganizationPaymentInfo', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONPAYMENTINFO,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OrganizationPaymentInfo)
  })
_sym_db.RegisterMessage(OrganizationPaymentInfo)

OrganizationAutoCharge = _reflection.GeneratedProtocolMessageType('OrganizationAutoCharge', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONAUTOCHARGE,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OrganizationAutoCharge)
  })
_sym_db.RegisterMessage(OrganizationAutoCharge)

Organization = _reflection.GeneratedProtocolMessageType('Organization', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATION,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Organization)
  })
_sym_db.RegisterMessage(Organization)

APIKey = _reflection.GeneratedProtocolMessageType('APIKey', (_message.Message,), {
  'DESCRIPTOR' : _APIKEY,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.APIKey)
  })
_sym_db.RegisterMessage(APIKey)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.User)
  })
_sym_db.RegisterMessage(User)

CostData = _reflection.GeneratedProtocolMessageType('CostData', (_message.Message,), {
  'DESCRIPTOR' : _COSTDATA,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CostData)
  })
_sym_db.RegisterMessage(CostData)

UsageMetric = _reflection.GeneratedProtocolMessageType('UsageMetric', (_message.Message,), {
  'DESCRIPTOR' : _USAGEMETRIC,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UsageMetric)
  })
_sym_db.RegisterMessage(UsageMetric)

CostTotal = _reflection.GeneratedProtocolMessageType('CostTotal', (_message.Message,), {
  'DESCRIPTOR' : _COSTTOTAL,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CostTotal)
  })
_sym_db.RegisterMessage(CostTotal)

TotalMetricsData = _reflection.GeneratedProtocolMessageType('TotalMetricsData', (_message.Message,), {
  'DESCRIPTOR' : _TOTALMETRICSDATA,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TotalMetricsData)
  })
_sym_db.RegisterMessage(TotalMetricsData)

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {
  'DESCRIPTOR' : _METRICS,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Metrics)
  })
_sym_db.RegisterMessage(Metrics)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

GetOrganizationRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetOrganizationRequest)
  })
_sym_db.RegisterMessage(GetOrganizationRequest)

GetMetricsRequest = _reflection.GeneratedProtocolMessageType('GetMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICSREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetMetricsRequest)
  })
_sym_db.RegisterMessage(GetMetricsRequest)

APIKeyRequest = _reflection.GeneratedProtocolMessageType('APIKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.APIKeyRequest)
  })
_sym_db.RegisterMessage(APIKeyRequest)

APIKeyFindRequest = _reflection.GeneratedProtocolMessageType('APIKeyFindRequest', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYFINDREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.APIKeyFindRequest)
  })
_sym_db.RegisterMessage(APIKeyFindRequest)

UpdateDefaultOrganizationRequest = _reflection.GeneratedProtocolMessageType('UpdateDefaultOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDEFAULTORGANIZATIONREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateDefaultOrganizationRequest)
  })
_sym_db.RegisterMessage(UpdateDefaultOrganizationRequest)

ClientSettings = _reflection.GeneratedProtocolMessageType('ClientSettings', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSETTINGS,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClientSettings)
  })
_sym_db.RegisterMessage(ClientSettings)

CreateAutoChargeIntentRequest = _reflection.GeneratedProtocolMessageType('CreateAutoChargeIntentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAUTOCHARGEINTENTREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateAutoChargeIntentRequest)
  })
_sym_db.RegisterMessage(CreateAutoChargeIntentRequest)

CreateChargeRequest = _reflection.GeneratedProtocolMessageType('CreateChargeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHARGEREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateChargeRequest)
  })
_sym_db.RegisterMessage(CreateChargeRequest)

GetChargesRequest = _reflection.GeneratedProtocolMessageType('GetChargesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHARGESREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetChargesRequest)
  })
_sym_db.RegisterMessage(GetChargesRequest)

Charge = _reflection.GeneratedProtocolMessageType('Charge', (_message.Message,), {
  'DESCRIPTOR' : _CHARGE,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Charge)
  })
_sym_db.RegisterMessage(Charge)

Charges = _reflection.GeneratedProtocolMessageType('Charges', (_message.Message,), {
  'DESCRIPTOR' : _CHARGES,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Charges)
  })
_sym_db.RegisterMessage(Charges)

GetAutoChargeRequest = _reflection.GeneratedProtocolMessageType('GetAutoChargeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTOCHARGEREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetAutoChargeRequest)
  })
_sym_db.RegisterMessage(GetAutoChargeRequest)

AutoChargeIntent = _reflection.GeneratedProtocolMessageType('AutoChargeIntent', (_message.Message,), {
  'DESCRIPTOR' : _AUTOCHARGEINTENT,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AutoChargeIntent)
  })
_sym_db.RegisterMessage(AutoChargeIntent)

UpdateUserInfoRequest = _reflection.GeneratedProtocolMessageType('UpdateUserInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERINFOREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateUserInfoRequest)
  })
_sym_db.RegisterMessage(UpdateUserInfoRequest)

UserPasswordChangeTicket = _reflection.GeneratedProtocolMessageType('UserPasswordChangeTicket', (_message.Message,), {
  'DESCRIPTOR' : _USERPASSWORDCHANGETICKET,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UserPasswordChangeTicket)
  })
_sym_db.RegisterMessage(UserPasswordChangeTicket)

ListOrganizationMembersRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationMembersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTORGANIZATIONMEMBERSREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ListOrganizationMembersRequest)
  })
_sym_db.RegisterMessage(ListOrganizationMembersRequest)

RemoveOrganizationMemberRequest = _reflection.GeneratedProtocolMessageType('RemoveOrganizationMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEORGANIZATIONMEMBERREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.RemoveOrganizationMemberRequest)
  })
_sym_db.RegisterMessage(RemoveOrganizationMemberRequest)

RemoveOrganizationMemberResponse = _reflection.GeneratedProtocolMessageType('RemoveOrganizationMemberResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEORGANIZATIONMEMBERRESPONSE,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.RemoveOrganizationMemberResponse)
  })
_sym_db.RegisterMessage(RemoveOrganizationMemberResponse)

AddOrganizationMemberRequest = _reflection.GeneratedProtocolMessageType('AddOrganizationMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDORGANIZATIONMEMBERREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AddOrganizationMemberRequest)
  })
_sym_db.RegisterMessage(AddOrganizationMemberRequest)

UpdateOrganizationMemberRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONMEMBERREQUEST,
  '__module__' : 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateOrganizationMemberRequest)
  })
_sym_db.RegisterMessage(UpdateOrganizationMemberRequest)

_DASHBOARDSERVICE = DESCRIPTOR.services_by_name['DashboardService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014./;dashboard'
  _ORGANIZATIONROLE._serialized_start=3170
  _ORGANIZATIONROLE._serialized_end=3227
  _ORGANIZATIONMEMBER._serialized_start=29
  _ORGANIZATIONMEMBER._serialized_end=198
  _ORGANIZATIONGRANT._serialized_start=200
  _ORGANIZATIONGRANT._serialized_end=304
  _ORGANIZATIONPAYMENTINFO._serialized_start=306
  _ORGANIZATIONPAYMENTINFO._serialized_end=392
  _ORGANIZATIONAUTOCHARGE._serialized_start=394
  _ORGANIZATIONAUTOCHARGE._serialized_end=467
  _ORGANIZATION._serialized_start=470
  _ORGANIZATION._serialized_end=786
  _APIKEY._serialized_start=788
  _APIKEY._serialized_end=848
  _USER._serialized_start=851
  _USER._serialized_end=1098
  _COSTDATA._serialized_start=1100
  _COSTDATA._serialized_end=1157
  _USAGEMETRIC._serialized_start=1160
  _USAGEMETRIC._serialized_end=1346
  _COSTTOTAL._serialized_start=1348
  _COSTTOTAL._serialized_end=1406
  _TOTALMETRICSDATA._serialized_start=1408
  _TOTALMETRICSDATA._serialized_end=1509
  _METRICS._serialized_start=1511
  _METRICS._serialized_end=1601
  _EMPTYREQUEST._serialized_start=1603
  _EMPTYREQUEST._serialized_end=1617
  _GETORGANIZATIONREQUEST._serialized_start=1619
  _GETORGANIZATIONREQUEST._serialized_end=1655
  _GETMETRICSREQUEST._serialized_start=1658
  _GETMETRICSREQUEST._serialized_end=1811
  _APIKEYREQUEST._serialized_start=1813
  _APIKEYREQUEST._serialized_end=1847
  _APIKEYFINDREQUEST._serialized_start=1849
  _APIKEYFINDREQUEST._serialized_end=1880
  _UPDATEDEFAULTORGANIZATIONREQUEST._serialized_start=1882
  _UPDATEDEFAULTORGANIZATIONREQUEST._serialized_end=1941
  _CLIENTSETTINGS._serialized_start=1943
  _CLIENTSETTINGS._serialized_end=1977
  _CREATEAUTOCHARGEINTENTREQUEST._serialized_start=1980
  _CREATEAUTOCHARGEINTENTREQUEST._serialized_end=2108
  _CREATECHARGEREQUEST._serialized_start=2110
  _CREATECHARGEREQUEST._serialized_end=2172
  _GETCHARGESREQUEST._serialized_start=2174
  _GETCHARGESREQUEST._serialized_end=2256
  _CHARGE._serialized_start=2258
  _CHARGE._serialized_end=2380
  _CHARGES._serialized_start=2382
  _CHARGES._serialized_end=2425
  _GETAUTOCHARGEREQUEST._serialized_start=2427
  _GETAUTOCHARGEREQUEST._serialized_end=2474
  _AUTOCHARGEINTENT._serialized_start=2477
  _AUTOCHARGEINTENT._serialized_end=2621
  _UPDATEUSERINFOREQUEST._serialized_start=2623
  _UPDATEUSERINFOREQUEST._serialized_end=2676
  _USERPASSWORDCHANGETICKET._serialized_start=2678
  _USERPASSWORDCHANGETICKET._serialized_end=2720
  _LISTORGANIZATIONMEMBERSREQUEST._serialized_start=2722
  _LISTORGANIZATIONMEMBERSREQUEST._serialized_end=2786
  _REMOVEORGANIZATIONMEMBERREQUEST._serialized_start=2788
  _REMOVEORGANIZATIONMEMBERREQUEST._serialized_end=2870
  _REMOVEORGANIZATIONMEMBERRESPONSE._serialized_start=2872
  _REMOVEORGANIZATIONMEMBERRESPONSE._serialized_end=2906
  _ADDORGANIZATIONMEMBERREQUEST._serialized_start=2908
  _ADDORGANIZATIONMEMBERREQUEST._serialized_end=3028
  _UPDATEORGANIZATIONMEMBERREQUEST._serialized_start=3031
  _UPDATEORGANIZATIONMEMBERREQUEST._serialized_end=3168
  _DASHBOARDSERVICE._serialized_start=3230
  _DASHBOARDSERVICE._serialized_end=4777
# @@protoc_insertion_point(module_scope)
