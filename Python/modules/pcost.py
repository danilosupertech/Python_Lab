# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost


# This code only runs when the file is executed as a script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
