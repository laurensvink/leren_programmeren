#from recipe_lib import str_amount_fraction
from recipe_lib import str_amount_fraction
# Constanten
TXT_SPOONS = "spoon|spoons"
TXT_TEASPOONS = "teaspoon|teaspoons"
TXT_CUPS = "cup|cups"


def str_single_plural(amount, text):
    single, plural = text.split("|")
    if amount >= 2:
        return plural
    else:
        return single


def str_units(amount, unit):
    if unit == "spoon":
        return str_single_plural(amount, TXT_SPOONS)
    elif unit == "teaspoon":
        return str_single_plural(amount, TXT_TEASPOONS)
    elif unit == "cup":
        return str_single_plural(amount, TXT_CUPS)
    else:
        return unit


def format_ingredient(amount, unit, text):
    amount_str = str_amount_fraction(amount)
    unit_str = str_units(amount, unit)
    name_str = str_single_plural(amount, text)

    return f"{amount_str} {unit_str} {name_str}"


# Testcases
if __name__ == "__main__":
    print(format_ingredient(1, "spoon", "egg|eggs"))       # 1 spoon egg
    print(format_ingredient(2, "spoon", "egg|eggs"))       # 2 spoons eggs
    print(format_ingredient(0.5, "cup", "milk|milk"))      # ½ cup milk
    print(format_ingredient(1.5, "teaspoon", "sugar|sugar"))  # 1½ teaspoons sugar