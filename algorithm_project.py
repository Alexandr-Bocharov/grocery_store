def get_elements(n: int):
    elements = ""
    cur_num = 1
    count = 0
    for i in range(n):
        if count == cur_num:
            cur_num += 1
            count = 0

        elements += str(cur_num)
        count += 1

    return elements


print(get_elements(29))
