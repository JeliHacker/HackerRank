def count_substring(string, sub_string):
    occurrences = 0
    left_pointer, right_pointer = 0, len(sub_string) - 1
    
    while sub_string in string[left_pointer:len(string)]:
        if left_pointer < len(string) and right_pointer < len(string):
            if string[left_pointer:right_pointer + 1] == sub_string:
                occurrences += 1
                left_pointer = right_pointer
                right_pointer += len(sub_string) - 1
            else:
                left_pointer += 1
                right_pointer += 1
    return occurrences            
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
