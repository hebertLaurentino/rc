import unittest
from roteador import verify_summarize, summarize_routes

class TestSumarizacao(unittest.TestCase):
    def test_summariza_adjacent_mesmo_prefixo(self):
        ok, net = verify_summarize("192.168.20.0/24", "192.168.21.0/24")
        self.assertTrue(ok)
        self.assertEqual(net, "192.168.20.0/23")

    def test_nao_summariza_prefixo_diferente(self):
        ok, net = verify_summarize("10.0.0.0/24", "10.0.1.0/25")
        self.assertFalse(ok)
        self.assertIsNone(net)

    def test_summarize_routes_somente_mesmo_next_hop(self):
        table = {
            "10.0.2.0/24": {"cost": 2, "next_hop": "127.0.0.1:5001"},
            "10.0.3.0/24": {"cost": 5, "next_hop": "127.0.0.1:5001"},
            "10.0.4.0/24": {"cost": 1, "next_hop": "127.0.0.1:5002"},
        }
        out = summarize_routes(table)
        self.assertIn("10.0.2.0/23", out)
        self.assertNotIn("10.0.2.0/24", out)
        self.assertNotIn("10.0.3.0/24", out)
        self.assertIn("10.0.4.0/24", out)
        self.assertEqual(out["10.0.2.0/23"]["cost"], 5)

if __name__ == "__main__":
    unittest.main()