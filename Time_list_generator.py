#    For CTF challenge. I needed a script to output every possible time in HH:MM:SS format to make a
#    list to run against a hash.
#
#
def main():                                 # Main Function
    for i in range(25):                     # i will represent the hours column
        if (i < 10):                        # This will check if a 0 needs to be added ex. 01 instead of 1
            i = str(0) + str(i)
        else:                               # Otherwise i will remain the same
            i = i
        for j in range(60):                 # j will represent the minutes column
            if (j < 10):                    # This will also check if a 0 needs to be added
                j = str(0) + str(j)
            else:                           # Otherwise keep it the same as it was
                j = j
            for k in range(60):             # k will represent the seconds column

                if (k < 10):                # Here we will also check and see if a 0 needs to be added
                    k = str(0) + str(k)
                else:                       # Otherwise keep original 2 digit number
                    k = k


                time = str(i) + ":" + str(j) + ":" + str(k)   # This is the debug and print section
                print(time)                                   # Lets print and see if it is correct



if __name__ == '__main__':                  # Run the script!!!!!!
    main()


