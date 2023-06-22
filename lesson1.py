# def count_elements(stroka):
#     print(set(stroka))
#     for sum in set(stroka):
#        counter = 0
#        for sub_e in stroka:
#            if sum == sub_e:
#                counter += 1
#        print(sum, '-', counter)

# count_elements('aabbcc')

def strcounter2(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    
    for sym, count in syms_counter.items():
        print(sym, '-', count)

strcounter2('aaaabbbbbccccc')