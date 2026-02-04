import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    try:
        data = pd.read_csv(path)
    except Exception as error:
        print(error)
        return

    return (data)


def main():
    print(load("../life_expectancy_years.csv"))


if (__name__ == "__main__"):
    main()
