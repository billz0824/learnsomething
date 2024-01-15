import unittest
import interface as it


class TestInterfaceMethods(unittest.TestCase):
    def setUp(self):
        self.market = it.Exchange(100, 100)

    def test_things(self):
        trade1 = it.Trade("Bill", "BUY", 100, 1)
        self.market.add_trade(trade1)
        self.assertEqual(self.market.accounts["Bill"][0], 100)
        self.assertEqual(self.market.accounts["Bill"][1], 100)
        trade2 = it.Trade("Dave", "SELL", 100, 1)
        self.market.add_trade(trade2)
        self.assertEqual(self.market.accounts["Bill"][0], 0)
        self.assertEqual(self.market.accounts["Bill"][1], 200)
        self.assertEqual(self.market.accounts["Dave"][0], 200)
        self.assertEqual(self.market.accounts["Dave"][1], 0)

    def test_invalid_trades(self):
        trade1 = it.Trade("Bill", "SELL", 100, 1)
        self.market.add_trade(trade1)
        self.assertEqual(self.market.accounts["Bill"][0], 100)
        self.assertEqual(self.market.accounts["Bill"][1], 100)
        trade2 = it.Trade("Dave", "BUY", 100, 1)
        self.market.add_trade(trade2)
        self.assertEqual(self.market.accounts["Bill"][0], 200)
        self.assertEqual(self.market.accounts["Bill"][1], 0)
        self.assertEqual(self.market.accounts["Dave"][0], 0)
        self.assertEqual(self.market.accounts["Dave"][1], 200)
        wrong_trade = it.Trade("Bill", "SELL", 100, 2)
        with self.assertRaises(ValueError):
            self.market.add_trade(wrong_trade)
        wrong_trade = it.Trade("Dave", "BUY", 100, 2)
        with self.assertRaises(ValueError):
            self.market.add_trade(wrong_trade)
        wrong_trade = it.Trade("Trent", "SELL", 2600040, .2)
        with self.assertRaises(ValueError):
            self.market.add_trade(wrong_trade)



if __name__ == '__main__':
    unittest.main()
