def make_binary(length):
    if length == 0:
        return [""]
    else:
        all_but_first = make_binary(length - 1)
        answer = []
        for bits in all_but_first:
            answer.append("0" + bits)
        for bits in all_but_first:
            answer.append("1" + bits)
        return answer

#print make_binary(4)


def bin_to_dec(bin_num):
    if len(bin_num) == 0:
        return 0
    else:
        dec_eq = int(bin_num[0]) * 2 ** (len(bin_num) - 1) + bin_to_dec(bin_num[1:])
        return dec_eq


def make_gray(length):
    if length == 0:
        return [""]
    else:
        all_but_first = make_gray(length - 1)
        answer = []
        for bits in all_but_first:
            answer.append("0" + bits)
        all_but_first.reverse()
        for bits in all_but_first:
            answer.append("1" + bits)
        return answer


def gray_to_bin(gray_code):
    if len(gray_code) <= 1:
        return gray_code
    else:
        mod_significant_bit = (int(gray_code[0]) + int(gray_code[1])) % 2
        bin_num = gray_code[0] + gray_to_bin(str(mod_significant_bit) + gray_code[2:])
        return bin_num

def run_examples():
    length = 5
    print "Binary numbers of length :", length
    bin_list = make_binary(length)
    print bin_list

    print
    print "Decimal equivalent upto :", 2 ** length
    print [bin_to_dec(bin_num) for bin_num in bin_list]

    print
    print "Gray codes of length", length
    gray_list = make_gray(length)
    print gray_list

    print
    print "Gray codes converted to binary numbers"
    print [gray_to_bin(gray_code) for gray_code in gray_list]

run_examples()


