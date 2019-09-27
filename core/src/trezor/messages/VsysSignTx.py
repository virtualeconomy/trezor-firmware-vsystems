# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class VsysSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 1005

    def __init__(
        self,
        address_n: List[int] = None,
        protocol: str = None,
        api: int = None,
        opc: str = None,
        transactionType: int = None,
        senderPublicKey: str = None,
        amount: int = None,
        fee: int = None,
        feeScale: int = None,
        recipient: str = None,
        timestamp: int = None,
        attachment: str = None,
        txId: str = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.protocol = protocol
        self.api = api
        self.opc = opc
        self.transactionType = transactionType
        self.senderPublicKey = senderPublicKey
        self.amount = amount
        self.fee = fee
        self.feeScale = feeScale
        self.recipient = recipient
        self.timestamp = timestamp
        self.attachment = attachment
        self.txId = txId

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('protocol', p.UnicodeType, 0),
            3: ('api', p.UVarintType, 0),
            4: ('opc', p.UnicodeType, 0),
            5: ('transactionType', p.UVarintType, 0),
            6: ('senderPublicKey', p.UnicodeType, 0),
            7: ('amount', p.UVarintType, 0),
            8: ('fee', p.UVarintType, 0),
            9: ('feeScale', p.UVarintType, 0),
            10: ('recipient', p.UnicodeType, 0),
            11: ('timestamp', p.UVarintType, 0),
            12: ('attachment', p.UnicodeType, 0),
            13: ('txId', p.UnicodeType, 0),
        }
