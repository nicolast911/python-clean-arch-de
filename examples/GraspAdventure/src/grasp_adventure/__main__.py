import argparse


def say_hi(name="world"):
    print(f"Hello, {name}!")


def main():
    parser = argparse.ArgumentParser(
        prog="grasp-adventure",
        description="A simple adventure game demonstrating GRASP (and other) patterns",
        epilog="Have fun!",
    )
    parser.add_argument(
        "-n", "--name", default="world", help="the name of the person to greet"
    )
    args = parser.parse_args()
    say_hi(args.name)


if __name__ == "__main__":
    main()
