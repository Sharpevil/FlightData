from csvsort import csvsort as your_good_friend_in_the_computer_who_sorts_arbitrarily_large_files_for_you

FILE_NAME_CSV = "../DATA/live_2018-01-20-20_32.csv"                      # must be replaced with path being used.
NEW_FILE_NAME_CSV = "../DATA/sorted_2018-01-20-20_32.csv"                # yes, this one too.

file = open(FILE_NAME_CSV, "r")         # "r" means read mode
your_good_friend_in_the_computer_who_sorts_arbitrarily_large_files_for_you(FILE_NAME_CSV, [7,0], output_filename=NEW_FILE_NAME_CSV, has_header=False)