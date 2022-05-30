import bittensor
import torch
from typing import Union, List, Tuple, Optional

from bittensor._serializer import serializer


class Synapse:
    """ Proto serializable class which specifies the function to be called on a recieving neuron
        as well as the method of serialization and packing of forward/backward request/responses.
    """

    # Unique proto enum.
    synapse_type: bittensor.proto.Synapse.SynapseType = None

    def __init__(
        self, 
        forward_request_serializer_type: 'bittensor.proto.Serializer.Type' = bittensor.proto.Serializer.MSGPACK,
        forward_response_serializer_type: 'bittensor.proto.Serializer.Type' = bittensor.proto.Serializer.MSGPACK,
        backward_request_serializer_type: 'bittensor.proto.Serializer.Type' = bittensor.proto.Serializer.MSGPACK,
        backward_response_serializer_type: 'bittensor.proto.Serializer.Type' = bittensor.proto.Serializer.MSGPACK,
    ) -> 'Synapse':  
        """ Synapse super class initializer.
            Args:
                forward_request_serializer_type (:obj:`bittensor.proto.Serializer.Type` of shape :obj:`(1)`, `optional`, :default: `bittensor.proto.Serializer.MSGPACK`):
                    Serializer used to pack torch tensors on forward request.
                forward_response_serializer_type (:obj:`bittensor.proto.Serializer.Type` of shape :obj:`(1)`, `optional`, :default: `bittensor.proto.Serializer.MSGPACK`):
                    Serializer used to pack torch tensors on forward response.
                backward_request_serializer_type (:obj:`bittensor.proto.Serializer.Type` of shape :obj:`(1)`, `optional`, :default: `bittensor.proto.Serializer.MSGPACK`):
                    Serializer used to pack torch tensors on forward request.
                backward_response_serializer_type (:obj:`bittensor.proto.Serializer.Type` of shape :obj:`(1)`, `optional`, :default: `bittensor.proto.Serializer.MSGPACK`):
                    Serialzer used to pack torch tensors on backward response.
            Returns:
                Synapse (:obj:`Synapse`, `required`):
                    Synapse super class.
        """
        # self.forward_request_serializer_type = forward_request_serializer_type
        # self.forward_response_serializer_type = forward_response_serializer_type
        # self.backward_request_serializer_type = backward_request_serializer_type
        # self.backward_response_serializer_type = backward_response_serializer_type

    def __repr__(self) -> str: return self.__str__()
    def __str__(self) -> str: return "Synapse"

    @staticmethod
    def deserialize_from_instance_proto ( isntance_proto: bittensor.proto.Synapse ) -> 'Synapse':
        """ Deserialzied the instance proto to an instance class.
            Args:
                isntance_proto (:obj:`bittensor.proto.Synapse` of shape :obj:`(1)`, `required`):
                    Synapse instance proto to be deserialized.
            Returns:
                synapse_instance_clasee (:obj:`torch.Tensor`, `required`):
                    Deserialized instance class.
        """
        raise NotImplementedError("deserialize_from_instance_proto should be implemented by the subclass.")

    @staticmethod
    def deserialize_from_wire_proto ( wire_proto: bittensor.proto.Synapse ) -> 'Synapse':
        """ Deserialzied the wire proto to an instance class.
            Args:
                wire_proto (:obj:`bittensor.proto.Synapse` of shape :obj:`(1)`, `required`):
                    Synapse wire proto to be deserialized.
            Returns:
                synapse_instance_clasee (:obj:`torch.Tensor`, `required`):
                    Deserialized instance class.
        """
        raise NotImplementedError("deserialize_from_wire_proto should be implemented by the subclass.")

    def serialize_to_instance_proto( self ) -> 'bittensor.proto.Synapse':
        """ Serializes the class instance to a Synapse instance proto.
            Returns:
                serialized_synapse_as_instance_proto (:obj:`torch.Tensor`, `required`):
                    Instance class serialized to a instance proto.
        """
        raise NotImplementedError("serialize_to_instance_proto should be implemented by the subclass.")

    def serialize_to_wire_proto( self ) -> 'bittensor.proto.Synapse':
        """ Serializes the class instance to a Synapse wire proto.
            Returns:
                serialized_synapse_as_wire_proto (:obj:`torch.Tensor`, `required`):
                    Instance class serialized to a wire proto.
        """
        raise NotImplementedError("serialize_to_wire_proto should be implemented by the subclass.")

    def nill_forward_response_tensor ( self, forward_request_tensor: torch.Tensor ) -> torch.Tensor:
        """ Returns a zeroed tensor used as response to a dendrite forward call when the call fails.
            Args:
                forward_request_tensor (:obj:`torch.Tensor`, `required`):
                    Tensor being sent as forward request.
            Returns:
                nill_forward_response_tensor (:obj:`torch.Tensor`, `required`):
                    Zeroed forward response tensor.
        """
        raise NotImplementedError("nill_forward_response_tensor should be implemented by the subclass.")

    def nill_backward_response_gradient ( self, forward_request_tensor : torch.Tensor ) -> torch.Tensor:
        """ Returns a zeroed tensor used as response to a dendrite backward call when the call fails.
            Args:
                forward_request_tensor  (:obj:`torch.Tensor`, `required`):
                    Tensor being sent as forward request.
            Returns:
                nill_backward_response_gradient  (:obj:`torch.Tensor`, `required`):
                    Zeroed backward response gradient.
        """
        raise NotImplementedError("nill_backward_response_tensor should be implemented by the subclass.")

    def check_forward_request_tensor     ( self, forward_request_tensor ): pass
    def check_forward_response_tensor    ( self, forward_request_tensor, forward_response_tensor ): pass
    def check_backward_request_gradient  ( self, forward_request_tensor, backward_request_gradient ): pass
    def check_backward_response_gradient  ( self, forward_request_tensor, backward_request_gradient ): pass
    def encode_forward_request_tensor    ( self, forward_request_tensor: torch.Tensor ) -> torch.Tensor: return forward_request_tensor
    def decode_forward_request_tensor    ( self, forward_request_tensor: torch.Tensor ) -> torch.Tensor: return forward_request_tensor
    def encode_forward_response_tensor   ( self, forward_response_tensor: torch.Tensor ) -> torch.Tensor: return forward_response_tensor
    def decode_forward_response_tensor   ( self, forward_response_tensor: torch.Tensor ) -> torch.Tensor: return forward_response_tensor
    def encode_backward_request_gradient ( self, backward_request_gradient: torch.Tensor ) -> torch.Tensor: return backward_request_gradient
    def decode_backward_request_gradient ( self, backward_request_gradient: torch.Tensor ) -> torch.Tensor: return backward_request_gradient
    def encode_backward_response_gradient ( self, backward_response_gradient: torch.Tensor ) -> torch.Tensor: return backward_response_gradient
    def decode_backward_response_gradient ( self, backward_response_gradient: torch.Tensor ) -> torch.Tensor: return backward_response_gradient

    def serialize_forward_request_tensor( self, forward_request_tensor: torch.Tensor ) -> Tuple[ 'bittensor.proto.Tensor', 'bittensor.proto.ReturnCode',  str ]:        
        pass
        # self.check_forward_request_tensor ( forward_request_tensor )
        # forward_request_tensor = self.encode_forward_request_tensor ( forward_request_tensor )
        # tensor_serialzier = bittensor.serializer( serializer_type = self.forward_request_serializer_type )
        # return tensor_serialzier.serialize( tensor_obj = forward_request_tensor, from_type = bittensor.proto.TensorType.TORCH )

    def deserialize_forward_request_tensor( self, forward_request_proto: bittensor.proto.Tensor ) -> Tuple[ 'torch.Tensor', 'bittensor.proto.ReturnCode',  str ]:
        """ Returns a torch.Tensor from wire proto.Tensor after relevant deserialization has been applied. """
        pass
        # tensor_deserialzier = bittensor.serializer( serializer_type = self.forward_request_serializer_type )
        # forward_request_tensor = tensor_deserialzier.deserialize( tensor_pb2 = forward_request_proto, to_type = bittensor.proto.TensorType.TORCH )
        # forward_request_tensor = self.decode_forward_request_tensor ( forward_request_tensor )
        # self.check_forward_request_tensor ( forward_request_tensor )
        # return forward_request_tensor

    def serialize_forward_response_tensor( self, forward_request_tensor: torch.Tensor, forward_response_tensor: torch.Tensor ) -> Tuple[ 'bittensor.proto.Tensor', 'bittensor.proto.ReturnCode',  str ]:
        """ Returns a bittensor.proto.Tensor to be sent on the wire after relevant serialization applied. """        
        pass
        # encoded_tensor = self.encode_forward_response_tensor ( forward_response_tensor )
        # self.check_forward_response_tensor ( forward_request_tensor, encoded_tensor )
        # tensor_serialzier = bittensor.serializer( serializer_type = self.forward_response_serializer_type )
        # return tensor_serialzier.serialize( tensor_obj = encoded_tensor, from_type = bittensor.proto.TensorType.TORCH )

    def deserialize_forward_response_proto( self, forward_request_tensor: torch.Tensor, forward_response_proto: bittensor.proto.Tensor ) -> Tuple[ 'torch.Tensor', 'bittensor.proto.ReturnCode',  str ]:
        """ Returns a torch.Tensor from wire proto.Tensor after relevant deserialization has been applied. """
        pass
        # tensor_deserialzier = bittensor.serializer( serializer_type = self.forward_response_serializer_type )
        # forward_response_tensor = tensor_deserialzier.deserialize( tensor_pb2 = forward_response_proto, to_type = bittensor.proto.TensorType.TORCH )
        # self.check_forward_response_tensor ( forward_request_tensor, forward_response_tensor )
        # forward_response_tensor = self.decode_forward_response_tensor ( forward_response_tensor )
        # return forward_response_tensor

    def serialize_backward_request_gradient( self, forward_request_tensor: torch.Tensor, backward_request_gradient: torch.Tensor ) -> Tuple[ 'bittensor.proto.Tensor', 'bittensor.proto.ReturnCode',  str ]:
        """ Returns a bittensor.proto.Tensor gradient to be sent on the wire after relevant serialization applied. """
        pass
        # self.check_backward_request_gradient ( forward_request_tensor, backward_request_gradient )
        # encoded_tensor = self.encode_backward_request_gradient ( backward_request_gradient )
        # tensor_serialzier = bittensor.serializer( serializer_type = self.forward_request_serializer_type )
        # return tensor_serialzier.serialize( tensor_obj = encoded_tensor, from_type = bittensor.proto.TensorType.TORCH )

    def deserialize_backward_request_gradient( self, forward_request_tensor: torch.Tensor, backward_request_proto: bittensor.proto.Tensor ) -> Tuple[ 'torch.Tensor', 'bittensor.proto.ReturnCode',  str ]:
        pass
        # tensor_deserialzier = bittensor.serializer( serializer_type = self.backward_request_serializer_type )
        # backward_request_gradient = tensor_deserialzier.deserialize( tensor_pb2 = backward_request_proto, to_type = bittensor.proto.TensorType.TORCH )
        # backward_request_gradient = self.decode_backward_request_gradient ( backward_request_gradient )
        # self.check_backward_request_gradient (forward_request_tensor,  backward_request_gradient )
        # return backward_request_gradient

    def empty(self):
        pass
        # tensor_deserialzier = bittensor.serializer( serializer_type = self.forward_request_serializer_type )
        # return tensor_deserialzier.empty()
