from recognition import find_target_face

names_here = find_target_face()
names_pass = names_here

def now_print():
    print("names_here")
    print(names_here)
    return names_here

with open('output.txt', 'w') as file:
    # Write data to the file
    file.write('This is some data.\n')
    for item in names_here:
        file.write(str(item) + '\n')
    file.write('More data on another line.')
# def pass_on():
#     print("names_passed")
#     return names_pass

now_print()