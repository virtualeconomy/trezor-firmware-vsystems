# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class VsysAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 1001

    def __init__(
        self,
        protocol: str = None,
        api: int = None,
        opc: str = None,
        address: str = None,
    ) -> None:
        self.protocol = protocol
        self.api = api
        self.opc = opc
        self.address = address

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('protocol', p.UnicodeType, 0),  # required
            2: ('api', p.UVarintType, 0),  # required
            3: ('opc', p.UnicodeType, 0),  # required
            4: ('address', p.UnicodeType, 0),
        }
