// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package generation

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// GenerationServiceClient is the client API for GenerationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type GenerationServiceClient interface {
	Generate(ctx context.Context, in *Request, opts ...grpc.CallOption) (GenerationService_GenerateClient, error)
	ChainGenerate(ctx context.Context, in *ChainRequest, opts ...grpc.CallOption) (GenerationService_ChainGenerateClient, error)
	EstimateCost(ctx context.Context, in *Request, opts ...grpc.CallOption) (*EstimateCostResponse, error)
}

type generationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewGenerationServiceClient(cc grpc.ClientConnInterface) GenerationServiceClient {
	return &generationServiceClient{cc}
}

func (c *generationServiceClient) Generate(ctx context.Context, in *Request, opts ...grpc.CallOption) (GenerationService_GenerateClient, error) {
	stream, err := c.cc.NewStream(ctx, &GenerationService_ServiceDesc.Streams[0], "/gooseai.GenerationService/Generate", opts...)
	if err != nil {
		return nil, err
	}
	x := &generationServiceGenerateClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type GenerationService_GenerateClient interface {
	Recv() (*Answer, error)
	grpc.ClientStream
}

type generationServiceGenerateClient struct {
	grpc.ClientStream
}

func (x *generationServiceGenerateClient) Recv() (*Answer, error) {
	m := new(Answer)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *generationServiceClient) ChainGenerate(ctx context.Context, in *ChainRequest, opts ...grpc.CallOption) (GenerationService_ChainGenerateClient, error) {
	stream, err := c.cc.NewStream(ctx, &GenerationService_ServiceDesc.Streams[1], "/gooseai.GenerationService/ChainGenerate", opts...)
	if err != nil {
		return nil, err
	}
	x := &generationServiceChainGenerateClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type GenerationService_ChainGenerateClient interface {
	Recv() (*Answer, error)
	grpc.ClientStream
}

type generationServiceChainGenerateClient struct {
	grpc.ClientStream
}

func (x *generationServiceChainGenerateClient) Recv() (*Answer, error) {
	m := new(Answer)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *generationServiceClient) EstimateCost(ctx context.Context, in *Request, opts ...grpc.CallOption) (*EstimateCostResponse, error) {
	out := new(EstimateCostResponse)
	err := c.cc.Invoke(ctx, "/gooseai.GenerationService/EstimateCost", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GenerationServiceServer is the server API for GenerationService service.
// All implementations must embed UnimplementedGenerationServiceServer
// for forward compatibility
type GenerationServiceServer interface {
	Generate(*Request, GenerationService_GenerateServer) error
	ChainGenerate(*ChainRequest, GenerationService_ChainGenerateServer) error
	EstimateCost(context.Context, *Request) (*EstimateCostResponse, error)
	mustEmbedUnimplementedGenerationServiceServer()
}

// UnimplementedGenerationServiceServer must be embedded to have forward compatible implementations.
type UnimplementedGenerationServiceServer struct {
}

func (UnimplementedGenerationServiceServer) Generate(*Request, GenerationService_GenerateServer) error {
	return status.Errorf(codes.Unimplemented, "method Generate not implemented")
}
func (UnimplementedGenerationServiceServer) ChainGenerate(*ChainRequest, GenerationService_ChainGenerateServer) error {
	return status.Errorf(codes.Unimplemented, "method ChainGenerate not implemented")
}
func (UnimplementedGenerationServiceServer) EstimateCost(context.Context, *Request) (*EstimateCostResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method EstimateCost not implemented")
}
func (UnimplementedGenerationServiceServer) mustEmbedUnimplementedGenerationServiceServer() {}

// UnsafeGenerationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to GenerationServiceServer will
// result in compilation errors.
type UnsafeGenerationServiceServer interface {
	mustEmbedUnimplementedGenerationServiceServer()
}

func RegisterGenerationServiceServer(s grpc.ServiceRegistrar, srv GenerationServiceServer) {
	s.RegisterService(&GenerationService_ServiceDesc, srv)
}

func _GenerationService_Generate_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(Request)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(GenerationServiceServer).Generate(m, &generationServiceGenerateServer{stream})
}

type GenerationService_GenerateServer interface {
	Send(*Answer) error
	grpc.ServerStream
}

type generationServiceGenerateServer struct {
	grpc.ServerStream
}

func (x *generationServiceGenerateServer) Send(m *Answer) error {
	return x.ServerStream.SendMsg(m)
}

func _GenerationService_ChainGenerate_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(ChainRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(GenerationServiceServer).ChainGenerate(m, &generationServiceChainGenerateServer{stream})
}

type GenerationService_ChainGenerateServer interface {
	Send(*Answer) error
	grpc.ServerStream
}

type generationServiceChainGenerateServer struct {
	grpc.ServerStream
}

func (x *generationServiceChainGenerateServer) Send(m *Answer) error {
	return x.ServerStream.SendMsg(m)
}

func _GenerationService_EstimateCost_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GenerationServiceServer).EstimateCost(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/gooseai.GenerationService/EstimateCost",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GenerationServiceServer).EstimateCost(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

// GenerationService_ServiceDesc is the grpc.ServiceDesc for GenerationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var GenerationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "gooseai.GenerationService",
	HandlerType: (*GenerationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "EstimateCost",
			Handler:    _GenerationService_EstimateCost_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Generate",
			Handler:       _GenerationService_Generate_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "ChainGenerate",
			Handler:       _GenerationService_ChainGenerate_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "generation.proto",
}
