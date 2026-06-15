from dexscreener import DexscreenerClient

client = DexscreenerClient()

print("Bot Started")

pairs = client.search_pairs("SOL")

for pair in pairs[:5]:
    print(pair.base_token.name)
