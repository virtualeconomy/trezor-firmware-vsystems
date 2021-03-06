# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class VsysTransaction(p.MessageType):

    def __init__(
        self,
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
            1: ('protocol', p.UnicodeType, 0),  # required
            2: ('api', p.UVarintType, 0),  # required
            3: ('opc', p.UnicodeType, 0),  # required
            4: ('transactionType', p.UVarintType, 0),  # required
            5: ('senderPublicKey', p.UnicodeType, 0),
            6: ('amount', p.UVarintType, 0),
            7: ('fee', p.UVarintType, 0),  # required
            8: ('feeScale', p.UVarintType, 0),  # required
            9: ('recipient', p.UnicodeType, 0),
            10: ('timestamp', p.UVarintType, 0),  # required
            11: ('attachment', p.UnicodeType, 0),
            12: ('txId', p.UnicodeType, 0),
        }
