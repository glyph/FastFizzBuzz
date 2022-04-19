def fizzbuzz() -> None:
    for counter in range(1, 1000000000):
        fizz = counter % 3 == 0
        buzz = counter % 5 == 0
        if fizz:
            print("Fizz", end="")
        if buzz:
            print("Buzz", end="")
        if not (fizz or buzz):
            print(counter, end="")
        print()

if __name__ == "__main__":
    fizzbuzz()
