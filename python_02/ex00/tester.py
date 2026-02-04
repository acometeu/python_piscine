from load_csv import load


def main():
    try:
        print(load("../life_expectancy_years.csv"))
        data = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        print(load(data))
        print(load("../population_total.csv"))
        print(load("../ouioui.csv"))
    except Exception as error:
        print(f"error : {error}")


if (__name__ == "__main__"):
    main()
