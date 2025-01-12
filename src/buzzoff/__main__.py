"""Buzzoff command line tool."""

import argparse


def main() -> None:
    """Run the CLI"""
    parser = argparse.ArgumentParser(
        prog="buzzoff", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("letters", help="the set of letters")
    parser.add_argument("-m", "--mandatory", help="mandatory letter(s)")
    parser.add_argument(
        "-l", "--length", type=int, default=4, help="minimum word length"
    )
    args = parser.parse_args()

    # import inside function to speed up CLI parsing
    from buzzoff import buzz  # pylint: disable=import-outside-toplevel)

    print(
        "\n".join(buzz(args.letters, minlength=args.length, mandatory=args.mandatory))
    )


if __name__ == "__main__":
    main()
