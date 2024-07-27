import unittest
from mockito import mock, when, verify
from app.services.claim_service import ClaimService
from app.models.claim import Claim

class TestClaimService(unittest.TestCase):
    def test_create_claim(self):
        claim_service = ClaimService()
        claim = mock(Claim)
        
        when(claim).description.thenReturn("Medical bill")
        when(claim).amount.thenReturn(100.0)

        result = claim_service.create_claim(claim)

        verify(claim, times=1).description
        verify(claim, times=1).amount
        self.assertIsNotNone(result)
