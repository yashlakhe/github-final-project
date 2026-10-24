# This script calculates simple interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)
# Additional Authors:
# yashlakhe

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# simple interest = p * t * r / 100


def calculate_simple_interest(p, t, r):
    return (p * t * r) / 100


if __name__ == "__main__":
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the time period (in years): "))
    r = float(input("Enter the rate of interest: "))

    interest = calculate_simple_interest(p, t, r)
    print("The simple interest is: {:.2f}".format(interest))
