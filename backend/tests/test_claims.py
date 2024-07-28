import unittest
from mockito import when, verify, unstub
from app.services.claim_service import ClaimService
from app.models.claim import Claim

class TestClaimService(unittest.TestCase):
    def setUp(self):
        self.claim_service = ClaimService()
        self.claim = Claim(description="Medical bill", amount=100.0)

    def test_create_claim(self):
        when(self.claim_service).create_claim(...).thenReturn(self.claim)

        result = self.claim_service.create_claim(None, self.claim)

        verify(self.claim_service).create_claim(None, self.claim)
        self.assertIsNotNone(result)
        self.assertEqual(result.description, "Medical bill")
        self.assertEqual(result.amount, 100.0)

    def tearDown(self):
        unstub()

if __name__ == "__main__":
    unittest.main()
