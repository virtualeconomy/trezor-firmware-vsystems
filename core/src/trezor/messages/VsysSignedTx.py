# Automatically generated by pb2py
# fmt: off
import protobuf as p
from apps.vsys.constants import PROTOCOL, OPC_SIGN

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class VsysSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 1004

    def __init__(
        self,
        api: int = None,
        signature: str = None
    ) -> None:
        self.protocol = PROTOCOL
        self.api = api
        self.opc = OPC_SIGN
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('protocol', p.UnicodeType, 0),
            2: ('api', p.UVarintType, 0),
            3: ('opc', p.UnicodeType, 0),
            4: ('signature', p.UnicodeType, 0),
        }
