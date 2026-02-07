import numpy as np

# s = stock price at maturity
# k = strike price

def forward_payoff(S, K):
    return S - K

# np.maximum because f: R^n -> R^n
# call option payoff (European style)
def call_payoff(S, K):
    return np.maximum(S - K, 0)

# put option payoff (European style)
def put_payoff(S, K):
    return np.maximum(K - S, 0)