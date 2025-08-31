
def basket_weight(baskets: dict[str, list[float]]) -> list[dict[str, str | float]]:
    if not baskets:
        return []

    result = [
        {"name": name, "weight": sum(weights)}
        for name, weights in baskets.items()
    ]

    result.sort(key=lambda fruit: fruit["weight"], reverse=True)
    return result


fruits = {"apple": [1, 2.3, 4, 5], "orange": [3], "banana": [4, 5, 6]}
print(basket_weight(fruits))
