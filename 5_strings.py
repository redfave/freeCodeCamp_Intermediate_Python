from timeit import default_timer as timer


my_string = """Hello \
World"""
print(my_string)
print(my_string[-2])
print(my_string[2:11:2])
print(my_string[::-1])
#my_string[0] = 'h' => TypeError: Strings are immutable

print('First o at :', my_string.find('o'))

string2 = 'how,are,you,doing'
print(' '.join(string2.split(',')))

char_list = ['a'] * 1000000
start = timer()
concatenated_string1 = ''
for c in char_list:
    concatenated_string1 += c
stop = timer()
slow_time = stop - start
print(slow_time)
start = timer()
concatenated_string2 = ''.join(char_list)
stop = timer()
fast_time = stop - start
print(fast_time)
print(f'Join is ca. {slow_time/fast_time:.0f} times faster than for loop')




