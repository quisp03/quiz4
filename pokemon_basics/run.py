from battle.base_attack import calc_attack_power
from training.level_up import level_increase
from exploring.item_navigation import item_search

def main():


    level = 5
    base_power = 10

    print(calc_attack_power(level, base_power))

    current_level = 5

    print(level_increase(current_level))

    items = ["Poke Ball", "Potions", "Index"]
    item_find = "Poke Ball"

    print(item_search(items, item_find))

if __name__ == "__main__":
    main()