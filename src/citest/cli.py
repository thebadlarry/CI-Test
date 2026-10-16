"""Command line: `citest 1 2 3` prints mean, median and rms."""

import argparse

from citest.stats import mean, median, rms


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="citest", description=__doc__)
    p.add_argument("values", nargs="+", type=float)
    args = p.parse_args(argv)
    print(f"mean={mean(args.values):g} median={median(args.values):g} rms={rms(args.values):g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
