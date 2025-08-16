def orden_lex(str_1, srt_2):
    if str_1 < str_2:
        return -1
    elif str_1 > str_2:
        return 1
    else:
        return 0

str_1 = input().lower()
str_2 = input().lower()

print(orden_lex(str_1,str_2))
