#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 1, 2023
# This program Calculates the cost of a pizza with
# tax.


import constants


def main():
    # input - getting diameter
    d = int(input("What is the diameter of the pizza? "))

    # process - calculate subtotal
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + (constants.INGRED_COST * d)
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output - display cost
    print("the total cost of the pizza is {:.2f} dollars".format(total))


if __name__ == "__main__":
    main()
