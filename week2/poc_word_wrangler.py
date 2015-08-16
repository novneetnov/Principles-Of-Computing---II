"""
Student code for Word Wrangler game
"""

import urllib2
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    ans = []
    idx = 0
    while idx < len(list1):
        comp_idx = idx + 1
        if comp_idx < len(list1):
            while list1[idx] == list1[comp_idx]:
                comp_idx += 1
                if comp_idx == len(list1):
                    break
        ans.append(list1[idx])
        idx = comp_idx
    return ans


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    ans = []
    idx_lst1 = 0
    idx_lst2 = 0
    while idx_lst1 < len(list1):
        if idx_lst2 == len(list2):
            break
        while idx_lst2 < len(list2):
            if list1[idx_lst1] < list2[idx_lst2]:
                idx_lst1 += 1
                break
            elif list1[idx_lst1] == list2[idx_lst2]:
                ans.append(list1[idx_lst1])
                idx_lst1 += 1
                idx_lst2 += 1
                break
            idx_lst2 += 1
    return ans

# Functions to perform merge sort


def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    ans = []
    temp_list1 = list(list1)
    temp_list2 = list(list2)
    while temp_list1:
        if not temp_list2:
            ans.extend(temp_list1)
            return ans
        if temp_list1[0] < temp_list2[0]:
            ans.append(temp_list1.pop(0))
        elif temp_list2[0] < temp_list1[0]:
            ans.append(temp_list2.pop(0))
        else:
            ans.append(temp_list1.pop(0))
            ans.append(temp_list2.pop(0))
    ans.extend(temp_list2)
    return ans


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list(list1)
    else:
        sub_list1 = merge_sort(list1[0:len(list1) / 2])
        sub_list2 = merge_sort(list1[len(list1) / 2:])
        sorted_list = merge(sub_list1, sub_list2)
        return sorted_list

# Function to generate all strings for the word wrangler game


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) < 1:
        return [""]
    else:
        ans = []
        first_char = word[0]
        rest_all_strings = gen_all_strings(word[1:])
        for string in rest_all_strings:
            for idx in range(len(string) + 1):
                new_word = string[0:idx] + first_char + string[idx:]
                ans.append(new_word)
        ans.extend(rest_all_strings)
    return ans

# Function to load words from a file


def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    #If file not accessible through internet, use the one in the 'res' folder.
    word_list = []
    url = codeskulptor.file2url(WORDFILE)
    netfile = urllib2.urlopen(url)
    data = netfile.readlines()
    for word in data:
        word_list.append(word[:-1])
    return word_list


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    
