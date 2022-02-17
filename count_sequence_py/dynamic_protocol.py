"""
Dynamic Program to Instruct user how to prepare a 3 ml solution of
10 mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.
"""


def calc_func():
    """
    This is the main function for calculating concentrations
    """
    print("Add " + str(FINAL_VOL * (NA_CL_FINAL / NA_CL_STOCK)) + " ml NaCl")
    print("Add " + str(FINAL_VOL * (MG_FINAL / MG_STOCK)) + " ml MgCl2")
    print("Add water to a final volume of " + str(FINAL_VOL) + " ml and mix")


if __name__ == "__main__":

    # getting concentration of all the reagents used from user
    FINAL_VOL = float(input("Please enter the final volume of the solution (ml): "))
    NA_CL_STOCK = float(input("Please enter the NaCl stock (mM): "))
    NA_CL_FINAL = float(input("Please enter the NaCl final (mM): "))
    MG_STOCK = float(input("Please enter the MgCl2 stock (mM): "))
    MG_FINAL = float(input("Please enter the MgCl2 final (mM): "))

    # calling main function
    calc_func()
