import requests
import time

def get_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    return requests.get(url).json().get("pairs", [])


def score(pair):
    liquidity = pair.get("liquidity", {}).get("usd", 0)
    volume = pair.get("volume", {}).get("h24", 0)
    change = pair.get("priceChange", {}).get("h24", 0)

    score = 0

    if liquidity > 50000:
        score += 30
    elif liquidity > 10000:
        score += 15

    if volume > 100000:
        score += 30
    elif volume > 20000:
        score += 15

    if change > 20:
        score += 25
    elif change > 5:
        score += 10

    return score


def run():
    pairs = get_pairs()
    results = []

    for p in pairs[:50]:
        try:
            s = score(p)

            results.append({
                "name": p.get("baseToken", {}).get("name"),
                "symbol": p.get("baseToken", {}).get("symbol"),
                "score": s,
                "liquidity": p.get("liquidity", {}).get("usd", 0),
                "volume": p.get("volume", {}).get("h24", 0),
                "change": p.get("priceChange", {}).get("h24", 0),
                "url": p.get("url")
            })
        except:
            pass

    results.sort(key=lambda x: x["score"], reverse=True)

    for r in results[:10]:
        print(r)


if __name__ == "__main__":
    while True:
        print("\n🔍 scanning market...\n")
        run()
        time.sleep(300)
