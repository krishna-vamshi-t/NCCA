import argparse
from pipeline.run_pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(description="Netflix Churn Analysis Pipeline")
    parser.add_argument(
        "--mode",
        type=str,
        default="full",
        choices=["full", "metrics-only"],
        help="Run mode: 'full' runs everything, 'metrics-only' skips segmentation"
    )
    args = parser.parse_args()

    print(f"\n[CONFIG] Running in mode: {args.mode}\n")
    run_pipeline(mode=args.mode)


if __name__ == "__main__":
    main()