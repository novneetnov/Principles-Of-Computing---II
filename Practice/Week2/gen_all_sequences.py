def gen_all_sequences(outcomes, length):
    if length == 0:
        return set([()])
    else:
        answer_list = []
        all_but_first = gen_all_sequences(outcomes, length - 1)
        for seq in all_but_first:
            for outcome in outcomes:
                temp_seq = list(seq)
                temp_seq.append(outcome)
                answer_list.append(tuple(temp_seq))
        return set(answer_list)


def gen_all_permutations(outcomes, length):
    if length == 0:
        return set([()])
    else:
        answer_list = []
        all_but_first = gen_all_permutations(outcomes, length - 1)
        for seq in all_but_first:
            for outcome in outcomes:
                if seq.count(outcome) == 0:
                    temp_seq = list(seq)
                    temp_seq.append(outcome)
                    answer_list.append(tuple(temp_seq))
        return set(answer_list)

def gen_all_permutations_special_case(outcomes, length):
    """
    Special case of len(outcomes) = length
    """
    if length == 0:
        return set([()])
    else:
        rest_permutations = gen_all_permutations_special_case(outcomes[1:], length - 1)
        answer = []
        for perm in rest_permutations:
            for idx in range(len(perm) + 1):
                perm_list = list(perm)
                new_perm_list = perm_list[0:idx] + [outcomes[0]] + perm_list[idx:]
                answer.append(tuple(new_perm_list))
        return set(answer)


def gen_all_combinations(outcomes, length):
    if length == 0:
        return set([()])
    else:
        answer_list = []
        all_but_first = gen_all_combinations(outcomes, length - 1)
        for seq in all_but_first:
            for outcome in outcomes:
                if seq.count(outcome) == 0:
                    temp_seq = list(seq)
                    temp_seq.append(outcome)
                    answer_list.append(tuple(sorted(temp_seq)))
        return set(answer_list)


def run_example(outcomes, length):
    print "All Sequences from", outcomes, "and of length", length, ":"
    all_seq = gen_all_sequences(outcomes, length)
    print len(all_seq)

    print
    print "All Permutations "
    all_permutations = gen_all_permutations(outcomes, length)
    print len(all_permutations)

    print
    print "All Combinations"
    all_combinations = gen_all_combinations(outcomes, length)
    print all_combinations

    print
    print "All Permutations Special Case"
    all_permutations = gen_all_permutations_special_case(outcomes, length)
    print len(all_permutations)

run_example([1, 2, 3, 4], 4)