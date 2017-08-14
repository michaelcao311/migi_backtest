class Eth:

    eth_price = 0
    tx_fee_ratio = 1.0025

    def __init__(self, initial_usd=10000):
        self.usd = initial_usd
        self.eth = 0
        self.data

    def buy(self, amount):
        cost = amount * self.eth_price * self.tx_fee_ratio
        if self.usd >= cost:
            self.usd -= cost
            self.eth += amount

    def sell(self, amount):
        if self.eth >= amount:
            self.eth -= amount
            self.usd += amount * self.eth_price * (1 / self.tx_fee_ratio)

    def update(self, data):
        self.data = data
        self.eth_price = float(data[-1:]['close'])