from sys import stdout
from typing import Tuple, Iterable


def compute_template() -> Iterable[bytes]:
    for counter in range(1, 16):
        fizz = counter % 3 == 0
        buzz = counter % 5 == 0
        if fizz:
            yield b"Fizz"
        if buzz:
            yield b"Buzz"
        if not (fizz or buzz):
            yield b"%d"
        yield b"\n"


chunk_copies = 4
precomputed_template_chunks = list(compute_template())
format_string = b"".join(precomputed_template_chunks)
number_indexes = [
    number_index
    for number_index, line_content in enumerate(format_string.split(b"\n"))
    if line_content == b"%d"
]
format_string *= chunk_copies


def fizzbuzz() -> None:
    num: int = 1
    output = stdout.buffer.write
    for num in range(1, 1000000001, 15 * chunk_copies):
        t: Tuple[int, ...] = tuple(
            (
                x + number_index
                for x in range(num, num + (15 * chunk_copies), 15)
                for number_index in number_indexes
            )
        )
        output(format_string % t)


if __name__ == "__main__":
    fizzbuzz()
