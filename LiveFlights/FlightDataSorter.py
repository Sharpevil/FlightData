from csvsort import csvsort as your_good_friend_in_the_computer_who_sorts_arbitrarily_large_files_for_you

def sorter(filename, new_filename):

    file = open(filename, "r")         # "r" means read mode
    your_good_friend_in_the_computer_who_sorts_arbitrarily_large_files_for_you(filename, [7,0], output_filename=new_filename, has_header=False)

data = '../DATA/'
filepaths = [data + 'live_2018-01-20-20_32_clean.csv', data + 'live_2018-01-30-13_20_clean.csv',
             data + 'live_2018-02-03-16_46_clean.csv', data + 'live_2018-02-23-13_10.new_clean.csv', data +
             'sorted_2018-01-20-20_32_clean.csv']

sorter(filepaths[3], 'sorted_' + filepaths[3])