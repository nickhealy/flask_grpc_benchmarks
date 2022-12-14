# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_benchmark.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14grpc_benchmark.proto\x12\x07service\"\x14\n\x12SimpleRequestInput\"&\n\x13SimpleRequestOutput\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x13\x43omplexRequestInput\x12\n\n\x02id\x18\x01 \x01(\x05\"\x80\x07\n\x14\x43omplexRequestOutput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\ngiven_name\x18\x03 \x01(\t\x12\x13\n\x0b\x66\x61mily_name\x18\x04 \x01(\t\x12\x0b\n\x03\x64ob\x18\x05 \x01(\t\x12\r\n\x05phone\x18\x06 \x01(\t\x12\x17\n\x0fprimary_account\x18\x07 \x01(\x05\x12\x14\n\x0c\x63olour_blind\x18\x08 \x01(\x08\x12!\n\x19last_seen_legal_terms_sbk\x18\t \x01(\t\x12&\n\x1elast_seen_legal_terms_exchange\x18\n \x01(\t\x12\x14\n\x0cmailing_list\x18\x0b \x01(\x08\x12\x19\n\x11show_backer_stake\x18\x0c \x01(\x08\x12\x16\n\x0e\x62onus_eligible\x18\r \x01(\x08\x12\x0f\n\x07\x63reated\x18\x0e \x01(\t\x12\x15\n\rlast_modified\x18\x0f \x01(\t\x12\x10\n\x08\x61pi_user\x18\x10 \x01(\x08\x12#\n\x1blast_seen_payment_terms_sbk\x18\x11 \x01(\t\x12(\n last_seen_payment_terms_exchange\x18\x12 \x01(\t\x12\x13\n\x0binstant_bet\x18\x13 \x01(\x08\x12%\n\x1dgraphs_use_member_odds_format\x18\x14 \x01(\x08\x12!\n\x19last_disabled_usage_alert\x18\x15 \x01(\t\x12\x14\n\x0chide_balance\x18\x16 \x01(\x08\x12\x1e\n\x16marketing_notification\x18\x17 \x01(\x08\x12!\n\x19\x62\x65t_activity_notification\x18\x18 \x01(\x08\x12#\n\x1bpayment_status_notification\x18\x19 \x01(\x08\x12\x15\n\rmarketing_sms\x18\x1a \x01(\x08\x12\x10\n\x08\x66ullname\x18\x1b \x01(\t\x12\x17\n\x0fhas_national_id\x18\x1c \x01(\x08\x12\x11\n\tsuspended\x18\x1d \x01(\x08\x12\x10\n\x08\x65xcluded\x18\x1e \x01(\x08\x12\x0f\n\x07timeout\x18\x1f \x01(\x08\x12\x10\n\x08inactive\x18  \x01(\x08\x12\x0f\n\x07\x63ountry\x18! \x01(\t\x12\x14\n\x0chas_password\x18\" \x01(\x08\x12\x19\n\x11signup_ip_address\x18# \x01(\t\x12\x13\n\x0b\x66ingerprint\x18$ \x01(\t2\xa8\x01\n\x07Service\x12L\n\rSimpleRequest\x12\x1b.service.SimpleRequestInput\x1a\x1c.service.SimpleRequestOutput\"\x00\x12O\n\x0e\x43omplexRequest\x12\x1c.service.ComplexRequestInput\x1a\x1d.service.ComplexRequestOutput\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_benchmark_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIMPLEREQUESTINPUT._serialized_start=33
  _SIMPLEREQUESTINPUT._serialized_end=53
  _SIMPLEREQUESTOUTPUT._serialized_start=55
  _SIMPLEREQUESTOUTPUT._serialized_end=93
  _COMPLEXREQUESTINPUT._serialized_start=95
  _COMPLEXREQUESTINPUT._serialized_end=128
  _COMPLEXREQUESTOUTPUT._serialized_start=131
  _COMPLEXREQUESTOUTPUT._serialized_end=1027
  _SERVICE._serialized_start=1030
  _SERVICE._serialized_end=1198
# @@protoc_insertion_point(module_scope)
