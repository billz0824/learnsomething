from sortedcontainers import SortedList


class Exchange:

    def __init__(self, initial_balance, initial_shares):
        """Initial Balance is the amount that each account should start with."""
        self.initial_balance = initial_balance
        self.initial_shares = initial_shares
        self.accounts = {}
        self.sell = SortedList()
        self.buy = SortedList()
        self.trades = []

    def add_trade(self, trade):
        """Adds a trade to the exchange (validation required)
        and returns a match if required. It is up to you on how you will
        handle representing trades. """
        # add new account
        if trade.account not in self.accounts:
            self.accounts[trade.account] = [self.initial_balance, self.initial_shares]

        # verify trade validity
        if trade.side != "BUY" and trade.side != "SELL":
            raise ValueError('Invalid trade.')
        if trade.volume <= 0 or trade.price < 0:
            raise ValueError('Invalid trade.')
        if trade.side == "SELL" and trade.volume > self.accounts[trade.account][1]:
            raise ValueError("Invalid Trade: not enough shares.")
        elif trade.side == "BUY" and trade.volume * trade.price > self.accounts[trade.account][0]:
            raise ValueError("Invalid Trade: not enough money.")
        self.trades.append(trade)

        # matched trades
        matches = []

        # deal with orders to buy
        if trade.side == "BUY":
            remain = trade.volume
            if len(self.sell) == 0:
                self.buy.add(trade)
            else:
                while remain > 0:
                    potential = self.sell.bisect_left(trade)
                    for tr in range(potential+1):
                        curr = self.sell[tr]
                        curr_p = curr.price
                        curr_v = curr.volume
                        if curr_v == remain:
                            self.sell.remove(curr)
                            self.accounts[curr.account][0] += curr_v * curr_p
                            self.accounts[curr.account][1] -= curr_v
                            self.accounts[trade.account][0] -= curr_v * curr_p
                            self.accounts[trade.account][1] += curr_v
                            matches.append(curr)
                            return matches
                        elif curr_v > remain:
                            curr.volume -= remain
                            self.accounts[curr.account][0] += remain * curr_p
                            self.accounts[curr.account][1] -= remain
                            self.accounts[trade.account][0] -= remain * curr_p
                            self.accounts[trade.account][1] += remain
                            matches.append(curr)
                            return matches
                        else:
                            self.sell.remove(curr)
                            self.accounts[curr.account][0] += curr_v * curr_p
                            self.accounts[curr.account][1] -= curr_v
                            self.accounts[trade.account][0] -= curr_v * curr_p
                            self.accounts[trade.account][1] += curr_v
                            matches.append(curr)
                            remain -= curr.volume
                    if remain > 0:
                        trade.volume = remain
                        self.buy.add(trade)
                        break
            return

        else:
            if len(self.buy) == 0:
                self.sell.add(trade)
            else:
                remain = trade.volume
                while remain > 0:
                    potential = self.buy.bisect_right(trade)
                    for tr in range(len(self.buy) - 1, len(self.buy) - potential - 1, -1):
                        curr = self.buy[tr]
                        curr_p = curr.price
                        curr_v = curr.volume
                        if curr_v == remain:
                            self.buy.remove(curr)
                            self.accounts[curr.account][0] -= curr_v * curr_p
                            self.accounts[curr.account][1] += curr_v
                            self.accounts[trade.account][0] += curr_v * curr_p
                            self.accounts[trade.account][1] -= curr_v
                            matches.append(curr)
                            return matches
                        elif curr_v > remain:
                            curr.volume -= remain
                            self.accounts[curr.account][0] -= remain * curr_p
                            self.accounts[curr.account][1] += remain
                            self.accounts[trade.account][0] += remain * curr_p
                            self.accounts[trade.account][1] -= remain
                            matches.append(curr)
                            return matches
                        else:
                            self.accounts[curr.account][0] -= curr_v * curr_p
                            self.accounts[curr.account][1] += curr_v
                            self.accounts[trade.account][0] += curr_v * curr_p
                            self.accounts[trade.account][1] -= curr_v
                            matches.append(curr)
                            remain -= curr.volume
                            self.buy.remove(curr)
                    if remain > 0:
                        trade.volume = remain
                        self.sell.add(trade)
                        break
            return True



class Trade(object):
    def __init__(self, account, side, volume, price):
        # verify trade validity
        side = side.upper()
        self.account = account
        self.side = side
        self.volume = volume
        self.price = price

    def __lt__(self, other):
        if self.price != other.price:
            return self.price < other.price
        return self.volume < other.volume

    def __repr__(self):
        return (f"Name: {self.account}, Side: {self.side}, "
                f"Volume: {self.volume}, Price: {self.price}")

    def __eq__(self, other):
        return (self.account == other.account
                and self.side == other.side
                and self.volume == other.volume
                and self.price == other.price)