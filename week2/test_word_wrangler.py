import math
import CourseraPoc2.util.poc_simpletest as simpletest
import poc_word_wrangler as wrangler

suite = simpletest.TestSuite()


def run_remove_duplicates():

    list1 = [2, 4, 6, 8, 10]
    suite.run_test(wrangler.remove_duplicates(list1), [2, 4, 6, 8, 10], "Test #1:")

    list1 = [2, 4, 4, 4, 4, 4, 6]
    suite.run_test(wrangler.remove_duplicates(list1), [2, 4, 6], "Test #2")

    list1 = []
    suite.run_test(wrangler.remove_duplicates(list1), [], "Test #3")

    list1 = ['a', 'a', 'a', 'a', 'a', 'a']
    suite.run_test(wrangler.remove_duplicates(list1), ['a'], "Test #4")

    list1 = [4, 'happy', 78, 'zoo']
    suite.run_test(wrangler.remove_duplicates(list1), [4, 'happy', 78, 'zoo'], "Test #5")

    suite.report_results()


def run_intersect():

    list1 = [5, 8, 10]
    list2 = [7, 8, 45, 90]
    suite.run_test(wrangler.intersect(list1, list2), [8], "Test #1")

    list1 = ['a', 'b', 'e', 'g', 'k', 'u', 'y', 'z']
    list2 = ['a', 'b', 'e', 'g', 'k', 'u', 'y', 'z']
    suite.run_test(wrangler.intersect(list1, list2), ['a', 'b', 'e', 'g', 'k', 'u', 'y', 'z'], "Test #2")

    list1 = []
    list2 = []
    suite.run_test(wrangler.intersect(list1, list2), [], "Test #3")

    list1 = ['a', 'b', 'e', 'g', 'k', 'u', 'y', 'z']
    list2 = ['d', 'e', 'g', 'k', 'u', 'w', 'x']
    suite.run_test(wrangler.intersect(list1, list2), ['e', 'g', 'k', 'u'], "Test #4")

    list1 = ['d', 'e', 'g', 'k', 'k', 'u', 'w', 'x']
    list2 = ['a', 'b', 'e', 'g', 'k', 'u', 'y', 'z']
    suite.run_test(wrangler.intersect(list1, list2), ['e', 'g', 'k', 'u'], "Test #5")

    suite.report_results()


def run_merge():

    list1 = [2, 4, 6, 8, 10]
    list2 = [1, 3, 5, 7, 9]
    suite.run_test(wrangler.merge(list1, list2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test #1")

    list1 = [1, 4, 5, 8, 10]
    list2 = [1, 3, 5, 7, 9]
    suite.run_test(wrangler.merge(list1, list2), [1, 1, 3, 4, 5, 5, 7, 8, 9, 10], "Test #2")

    list1 = []
    list2 = [1, 3, 5, 7, 9]
    suite.run_test(wrangler.merge(list1, list2), [1, 3, 5, 7, 9], "Test #3")

    list1 = []
    list2 = []
    suite.run_test(wrangler.merge(list1, list2), [], "Test #4")

    list1 = ['a', 'c', 'e', 'g', 'i']
    list2 = ['b', 'd', 'f', 'h', 'j']
    suite.run_test(wrangler.merge(list1, list2), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], "Test #5")

    suite.report_results()


def run_merge_sort():

    list1 = [7, 9, 8, 6, 10, 5, 2, 3, 1, 4]
    suite.run_test(wrangler.merge_sort(list1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test #1")

    list1 = ['k', 'y', 'f', 'u', 'a', 'e', 'q']
    suite.run_test(wrangler.merge_sort(list1), ['a', 'e', 'f', 'k', 'q', 'u', 'y'], "Test #2")

    list1 = []
    suite.run_test(wrangler.merge_sort(list1), [], "Test #3")

    list1 = []
    suite.run_test(wrangler.merge_sort(list1), [], "Test #3")

    suite.report_results()


def run_gen_all_strings():

    word = "myth"
    suite.run_test(len(wrangler.gen_all_strings(word)), [], "Test #1")

    word = "m"
    suite.run_test(wrangler.gen_all_strings(word), ["m"], "Test #2")

    word = "munfilrn"
    suite.run_test(len(wrangler.gen_all_strings(word)), [], "Test #3")

    suite.report_results()


def run_test():
    #run_remove_duplicates()
    #run_intersect()
    run_merge()
    #run_merge_sort()
    #run_gen_all_strings()

run_test()