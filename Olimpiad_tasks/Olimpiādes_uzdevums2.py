def parse_input():
    N = int(input("Enter the number of cars: "))
    while True:
        A = int(input("Enter the number of overtaking events: "))
        print("Enter overtaking events (car1 car2):")
        overtakings = [tuple(map(int, input().split())) for _ in range(A)]
        
        # Check if the number of overtakings matches A
        if len(overtakings) == A:
            break
        else:
            print(f"You entered {len(overtakings)} overtaking events, but expected {A}. Please re-enter.")

    return N, overtakings

def apply_overtakings(order, overtakings):
    for overtaking in overtakings:
        car1, car2 = overtaking
        if car1 not in order:
            order.insert(order.index(car2) + 1, car1)
        else:
            order.remove(car1)
            order.insert(order.index(car2) + 1, car1)
    return order

def generate_initial_order(N, overtakings):
    initial_order = list(range(N, 0, -1))
    reversed_overtakings = overtakings[::-1]
    return apply_overtakings(initial_order, reversed_overtakings)

def main():
    N, overtakings = parse_input()
    initial_order = generate_initial_order(N, overtakings)
    print("Initial order of cars:", " ".join(map(str, initial_order)))

if __name__ == "__main__":
    main()
