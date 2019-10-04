from common import *
from apps.common.paths import HARDENED

if not utils.BITCOIN_ONLY:
    from apps.vsys.helpers import get_address_from_public_key, validate_full_path, get_chain_id, validate_address


@unittest.skipUnless(not utils.BITCOIN_ONLY, "altcoin")
class TestVsysAddress(unittest.TestCase):
    def test_address_to_pubkey(self):
        # source of test data - vsys java SDK
        pubkey = "3NaHDL4hig5A9Dh3gLbycWnfxpPTBe4WgeAG5AgeXPbL"
        expected_address = "AU9fRxUciwuG6JvdnPBPb8BJXvfDn8oxwtn"
        address = get_address_from_public_key(pubkey, "T")

        self.assertEqual(address, expected_address)

        pubkey2 = "4iE3oZsGDmR36wDYukKSGM4V6dPrFT9GiqUv2TBt3nUX"
        expected_address2 = "AR5EhMHz7YmxC1mrXQ818s6kP81mQvpNuDJ"
        address2 = get_address_from_public_key(pubkey2, "M")

        self.assertEqual(address2, expected_address2)

    def test_paths(self):
        # 44'/360'/a'/0/0 (mainnet) or 44'/1'/a'/0/0 (testnet) is correct
        incorrect_paths = [
            [44 | HARDENED],
            [44 | HARDENED, 360 | HARDENED],
            [44 | HARDENED, 360 | HARDENED, 0],
            [44 | HARDENED, 360 | HARDENED, 0 | HARDENED, 0 | HARDENED],
            [44 | HARDENED, 360 | HARDENED, 0 | HARDENED, 0 | HARDENED, 0 | HARDENED],
            [44 | HARDENED, 360 | HARDENED, 0 | HARDENED, 1, 0],
            [44 | HARDENED, 360 | HARDENED, 0 | HARDENED, 0, 5],
            [44 | HARDENED, 360 | HARDENED, 9999 | HARDENED],
            [44 | HARDENED, 360 | HARDENED, 9999000 | HARDENED, 0, 0],
            [44 | HARDENED, 60 | HARDENED, 0 | HARDENED, 0, 0],
            [1 | HARDENED, 1 | HARDENED, 1 | HARDENED],
        ]
        correct_paths_mainnet = [
            [44 | HARDENED, 360 | HARDENED, 0 | HARDENED, 0, 0],
            [44 | HARDENED, 360 | HARDENED, 3 | HARDENED, 0, 0],
            [44 | HARDENED, 360 | HARDENED, 9 | HARDENED, 0, 0],
        ]

        correct_paths_testnet = [
            [44 | HARDENED, 1 | HARDENED, 0 | HARDENED, 0, 0],
            [44 | HARDENED, 1 | HARDENED, 3 | HARDENED, 0, 0],
            [44 | HARDENED, 1 | HARDENED, 9 | HARDENED, 0, 0],
        ]

        for path in incorrect_paths:
            self.assertFalse(validate_full_path(path))

        for path in correct_paths_mainnet:
            self.assertTrue(validate_full_path(path))
            self.assertEqual(get_chain_id(path), "M")

        for path in correct_paths_testnet:
            self.assertTrue(validate_full_path(path))
            self.assertEqual(get_chain_id(path), "T")

    def test_address(self):
        # source of test data - vsys java SDK
        self.assertTrue(validate_address("AR4Exapc1LnZ5nYkGwPvmpD7QZtEsdRQoGk", "M"))
        self.assertTrue(validate_address("AU6K3cTDvrtBVcXmYjk6XVGeegu8vg8B8wL", "T"))
        self.assertFalse(validate_address("invalid address", "M"))
        self.assertFalse(validate_address("AR4Exapc1LnZ5nYkGwPvmpD7QZtEsdRQoGk", "T"))
        self.assertFalse(validate_address("AU6K3cTDvrtBVcXmYjk6XVGeegu8vg8B8wL", "M"))


if __name__ == '__main__':
    unittest.main()
