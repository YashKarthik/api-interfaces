// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.20.3
// source: engines.proto

package engines

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Possible engine type
type EngineType int32

const (
	EngineType_TEXT           EngineType = 0
	EngineType_PICTURE        EngineType = 1
	EngineType_AUDIO          EngineType = 2
	EngineType_VIDEO          EngineType = 3
	EngineType_CLASSIFICATION EngineType = 4
	EngineType_STORAGE        EngineType = 5
)

// Enum value maps for EngineType.
var (
	EngineType_name = map[int32]string{
		0: "TEXT",
		1: "PICTURE",
		2: "AUDIO",
		3: "VIDEO",
		4: "CLASSIFICATION",
		5: "STORAGE",
	}
	EngineType_value = map[string]int32{
		"TEXT":           0,
		"PICTURE":        1,
		"AUDIO":          2,
		"VIDEO":          3,
		"CLASSIFICATION": 4,
		"STORAGE":        5,
	}
)

func (x EngineType) Enum() *EngineType {
	p := new(EngineType)
	*p = x
	return p
}

func (x EngineType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (EngineType) Descriptor() protoreflect.EnumDescriptor {
	return file_engines_proto_enumTypes[0].Descriptor()
}

func (EngineType) Type() protoreflect.EnumType {
	return &file_engines_proto_enumTypes[0]
}

func (x EngineType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use EngineType.Descriptor instead.
func (EngineType) EnumDescriptor() ([]byte, []int) {
	return file_engines_proto_rawDescGZIP(), []int{0}
}

type EngineTokenizer int32

const (
	EngineTokenizer_GPT2 EngineTokenizer = 0
	EngineTokenizer_PILE EngineTokenizer = 1
)

// Enum value maps for EngineTokenizer.
var (
	EngineTokenizer_name = map[int32]string{
		0: "GPT2",
		1: "PILE",
	}
	EngineTokenizer_value = map[string]int32{
		"GPT2": 0,
		"PILE": 1,
	}
)

func (x EngineTokenizer) Enum() *EngineTokenizer {
	p := new(EngineTokenizer)
	*p = x
	return p
}

func (x EngineTokenizer) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (EngineTokenizer) Descriptor() protoreflect.EnumDescriptor {
	return file_engines_proto_enumTypes[1].Descriptor()
}

func (EngineTokenizer) Type() protoreflect.EnumType {
	return &file_engines_proto_enumTypes[1]
}

func (x EngineTokenizer) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use EngineTokenizer.Descriptor instead.
func (EngineTokenizer) EnumDescriptor() ([]byte, []int) {
	return file_engines_proto_rawDescGZIP(), []int{1}
}

// Engine info struct
type EngineInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id          string          `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Owner       string          `protobuf:"bytes,2,opt,name=owner,proto3" json:"owner,omitempty"`
	Ready       bool            `protobuf:"varint,3,opt,name=ready,proto3" json:"ready,omitempty"`
	Type        EngineType      `protobuf:"varint,4,opt,name=type,proto3,enum=gooseai.EngineType" json:"type,omitempty"`
	Tokenizer   EngineTokenizer `protobuf:"varint,5,opt,name=tokenizer,proto3,enum=gooseai.EngineTokenizer" json:"tokenizer,omitempty"`
	Name        string          `protobuf:"bytes,6,opt,name=name,proto3" json:"name,omitempty"`
	Description string          `protobuf:"bytes,7,opt,name=description,proto3" json:"description,omitempty"`
}

func (x *EngineInfo) Reset() {
	*x = EngineInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_engines_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EngineInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EngineInfo) ProtoMessage() {}

func (x *EngineInfo) ProtoReflect() protoreflect.Message {
	mi := &file_engines_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EngineInfo.ProtoReflect.Descriptor instead.
func (*EngineInfo) Descriptor() ([]byte, []int) {
	return file_engines_proto_rawDescGZIP(), []int{0}
}

func (x *EngineInfo) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *EngineInfo) GetOwner() string {
	if x != nil {
		return x.Owner
	}
	return ""
}

func (x *EngineInfo) GetReady() bool {
	if x != nil {
		return x.Ready
	}
	return false
}

func (x *EngineInfo) GetType() EngineType {
	if x != nil {
		return x.Type
	}
	return EngineType_TEXT
}

func (x *EngineInfo) GetTokenizer() EngineTokenizer {
	if x != nil {
		return x.Tokenizer
	}
	return EngineTokenizer_GPT2
}

func (x *EngineInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *EngineInfo) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

type ListEnginesRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ListEnginesRequest) Reset() {
	*x = ListEnginesRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_engines_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ListEnginesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListEnginesRequest) ProtoMessage() {}

func (x *ListEnginesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_engines_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListEnginesRequest.ProtoReflect.Descriptor instead.
func (*ListEnginesRequest) Descriptor() ([]byte, []int) {
	return file_engines_proto_rawDescGZIP(), []int{1}
}

// Engine info list
type Engines struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Engine []*EngineInfo `protobuf:"bytes,1,rep,name=engine,proto3" json:"engine,omitempty"`
}

func (x *Engines) Reset() {
	*x = Engines{}
	if protoimpl.UnsafeEnabled {
		mi := &file_engines_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Engines) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Engines) ProtoMessage() {}

func (x *Engines) ProtoReflect() protoreflect.Message {
	mi := &file_engines_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Engines.ProtoReflect.Descriptor instead.
func (*Engines) Descriptor() ([]byte, []int) {
	return file_engines_proto_rawDescGZIP(), []int{2}
}

func (x *Engines) GetEngine() []*EngineInfo {
	if x != nil {
		return x.Engine
	}
	return nil
}

var File_engines_proto protoreflect.FileDescriptor

var file_engines_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x65, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x07, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x22, 0xdf, 0x01, 0x0a, 0x0a, 0x45, 0x6e, 0x67,
	0x69, 0x6e, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x6f, 0x77, 0x6e, 0x65, 0x72,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x6f, 0x77, 0x6e, 0x65, 0x72, 0x12, 0x14, 0x0a,
	0x05, 0x72, 0x65, 0x61, 0x64, 0x79, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x05, 0x72, 0x65,
	0x61, 0x64, 0x79, 0x12, 0x27, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x0e, 0x32, 0x13, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x45, 0x6e, 0x67, 0x69,
	0x6e, 0x65, 0x54, 0x79, 0x70, 0x65, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x36, 0x0a, 0x09,
	0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x69, 0x7a, 0x65, 0x72, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0e, 0x32,
	0x18, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65,
	0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x69, 0x7a, 0x65, 0x72, 0x52, 0x09, 0x74, 0x6f, 0x6b, 0x65, 0x6e,
	0x69, 0x7a, 0x65, 0x72, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x06, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63,
	0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64,
	0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x14, 0x0a, 0x12, 0x4c, 0x69,
	0x73, 0x74, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x22, 0x36, 0x0a, 0x07, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x12, 0x2b, 0x0a, 0x06, 0x65,
	0x6e, 0x67, 0x69, 0x6e, 0x65, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x13, 0x2e, 0x67, 0x6f,
	0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x49, 0x6e, 0x66, 0x6f,
	0x52, 0x06, 0x65, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x2a, 0x5a, 0x0a, 0x0a, 0x45, 0x6e, 0x67, 0x69,
	0x6e, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12, 0x08, 0x0a, 0x04, 0x54, 0x45, 0x58, 0x54, 0x10, 0x00,
	0x12, 0x0b, 0x0a, 0x07, 0x50, 0x49, 0x43, 0x54, 0x55, 0x52, 0x45, 0x10, 0x01, 0x12, 0x09, 0x0a,
	0x05, 0x41, 0x55, 0x44, 0x49, 0x4f, 0x10, 0x02, 0x12, 0x09, 0x0a, 0x05, 0x56, 0x49, 0x44, 0x45,
	0x4f, 0x10, 0x03, 0x12, 0x12, 0x0a, 0x0e, 0x43, 0x4c, 0x41, 0x53, 0x53, 0x49, 0x46, 0x49, 0x43,
	0x41, 0x54, 0x49, 0x4f, 0x4e, 0x10, 0x04, 0x12, 0x0b, 0x0a, 0x07, 0x53, 0x54, 0x4f, 0x52, 0x41,
	0x47, 0x45, 0x10, 0x05, 0x2a, 0x25, 0x0a, 0x0f, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x54, 0x6f,
	0x6b, 0x65, 0x6e, 0x69, 0x7a, 0x65, 0x72, 0x12, 0x08, 0x0a, 0x04, 0x47, 0x50, 0x54, 0x32, 0x10,
	0x00, 0x12, 0x08, 0x0a, 0x04, 0x50, 0x49, 0x4c, 0x45, 0x10, 0x01, 0x32, 0x50, 0x0a, 0x0e, 0x45,
	0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x3e, 0x0a,
	0x0b, 0x4c, 0x69, 0x73, 0x74, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x12, 0x1b, 0x2e, 0x67,
	0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x45, 0x6e, 0x67, 0x69, 0x6e,
	0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x10, 0x2e, 0x67, 0x6f, 0x6f, 0x73,
	0x65, 0x61, 0x69, 0x2e, 0x45, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x22, 0x00, 0x42, 0x0c, 0x5a,
	0x0a, 0x2e, 0x2f, 0x3b, 0x65, 0x6e, 0x67, 0x69, 0x6e, 0x65, 0x73, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_engines_proto_rawDescOnce sync.Once
	file_engines_proto_rawDescData = file_engines_proto_rawDesc
)

func file_engines_proto_rawDescGZIP() []byte {
	file_engines_proto_rawDescOnce.Do(func() {
		file_engines_proto_rawDescData = protoimpl.X.CompressGZIP(file_engines_proto_rawDescData)
	})
	return file_engines_proto_rawDescData
}

var file_engines_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_engines_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_engines_proto_goTypes = []interface{}{
	(EngineType)(0),            // 0: gooseai.EngineType
	(EngineTokenizer)(0),       // 1: gooseai.EngineTokenizer
	(*EngineInfo)(nil),         // 2: gooseai.EngineInfo
	(*ListEnginesRequest)(nil), // 3: gooseai.ListEnginesRequest
	(*Engines)(nil),            // 4: gooseai.Engines
}
var file_engines_proto_depIdxs = []int32{
	0, // 0: gooseai.EngineInfo.type:type_name -> gooseai.EngineType
	1, // 1: gooseai.EngineInfo.tokenizer:type_name -> gooseai.EngineTokenizer
	2, // 2: gooseai.Engines.engine:type_name -> gooseai.EngineInfo
	3, // 3: gooseai.EnginesService.ListEngines:input_type -> gooseai.ListEnginesRequest
	4, // 4: gooseai.EnginesService.ListEngines:output_type -> gooseai.Engines
	4, // [4:5] is the sub-list for method output_type
	3, // [3:4] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_engines_proto_init() }
func file_engines_proto_init() {
	if File_engines_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_engines_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EngineInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_engines_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ListEnginesRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_engines_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Engines); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_engines_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_engines_proto_goTypes,
		DependencyIndexes: file_engines_proto_depIdxs,
		EnumInfos:         file_engines_proto_enumTypes,
		MessageInfos:      file_engines_proto_msgTypes,
	}.Build()
	File_engines_proto = out.File
	file_engines_proto_rawDesc = nil
	file_engines_proto_goTypes = nil
	file_engines_proto_depIdxs = nil
}
