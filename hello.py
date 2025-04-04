#!/usr/bin/env python3
import sys
import argparse
import math


def hello_world():
    """Retorna a mensagem clássica de Hello World"""
    return "Hello, World! CI/CD Test Successful!"


def add_numbers(a: float, b: float) -> float:
    """Soma dois números"""
    return a + b


def factorial(n: int) -> int:
    """Calcula o fatorial de um número"""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    return math.factorial(n)


def is_palindrome(word: str) -> bool:
    """Verifica se uma palavra é um palíndromo"""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def main():
    parser = argparse.ArgumentParser(
        description="Advanced Hello World for CI/CD Testing"
    )
    parser.add_argument(
        "--test", action="store_true", help="Run all functions with test values"
    )
    parser.add_argument(
        "--add", nargs=2, type=float, metavar=("A", "B"), help="Add two numbers"
    )
    parser.add_argument(
        "--fact", type=int, metavar="N", help="Calculate factorial of N"
    )
    parser.add_argument(
        "--palindrome", type=str, metavar="WORD", help="Check if word is palindrome"
    )

    args = parser.parse_args()

    if args.test:
        # Modo de teste - executa todas as funções
        print(hello_world())
        print(f"2 + 3 = {add_numbers(2, 3)}")
        print(f"Factorial of 5 = {factorial(5)}")
        print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
        return 0

    if args.add:
        print(
            f"{args.add[0]} + {args.add[1]} = {add_numbers(args.add[0], args.add[1])}"
        )

    if args.fact is not None:
        try:
            print(f"Factorial of {args.fact} = {factorial(args.fact)}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    if args.palindrome:
        print(f"Is '{args.palindrome}' a palindrome? {is_palindrome(args.palindrome)}")

    if not any(vars(args).values()):
        print(hello_world())

    return 0


if __name__ == "__main__":
    sys.exit(main())
