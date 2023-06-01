# Task 1. Is the Word Singular or Plural?
def is_plural(word):
    strword = str(word)
    if strword.endswith('s'):
        return True
    else:
        return False


print(is_plural("changes"))
print(is_plural("change"))
print(is_plural("dudes"))
print(is_plural("magic"))
print('------------------')
# Task 2. Stuttering Function


def stutter(word):
    if len(word) < 2:
        return word
    stutteredWord = word[0:2] + '... ' + word[0:2] + '... '
    stutteredWord += word + '?'
    return stutteredWord


print(stutter('sample'))
print('------------------')
# Task 3. Return the Index of All Capital Letters


def index_of_caps(string):
    new_list = []
    for i in range(len(string)):
        if string[i].isupper():
            new_list.append(i)
    return new_list


print(index_of_caps("eQuINoX"))
print('------------------')
# Task 4. Filter Strings from Array


def filter_list(list_to_filter):
    return [x for x in list_to_filter if isinstance(x, int)]


print(filter_list(filter_list([1, 2, 3, "a", "b", 4])))
print(filter_list(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"])))
print(filter_list(filter_list(["Nothing", "here"])))
print('------------------')
# Task 5. Alphabet Soup


def alphabet_soup(soup):
    return ''.join(sorted(soup))


print(alphabet_soup("fgfdg"))

print('------------------')
# Task 7. Chat Room Status


def chatroom_status(chatroom):
    num_users = len(chatroom)
    if num_users == 0:
        return "no one online"
    elif num_users == 1:
        return f"{chatroom[0]} online"
    elif num_users == 2:
        return f"{chatroom[0]} and {chatroom[1]} online"
    else:
        return f"{chatroom[0]}, {chatroom[1]} and {num_users - 2} more online"


print(chatroom_status(["pap_ier44", "townieBOY", "panda321",
      "motor_bike5", "sandwichmaker833", "violinist91"]))
# Task 8. Nth Smallest Integer
print('------------------')


def nth_smallest(lst, n):
    if n < 1 or n > len(lst):
        return None
    else:
        lst.sort()
        return lst[n-1]


print(nth_smallest([2, 3, 5, 7], 4))
print('------------------')

# Task 9. Date Format


def format_date(date):
    date = date.split('/')
    date.reverse()
    c = '-'.join(date)
    return c


print(format_date('01/15/2019'))
print('------------------')


# Task 10. Stalactites or Stalagmites?
def mineral_formation(stones):
    if stones[0].count(1) > 0 and stones[len(stones)-1].count(1) > 0:
        return "both"
    elif stones[0].count(1) > 0:
        return "stalactites"
    elif stones[len(stones)-1].count(1) > 0:
        return "stalagmites"


print(mineral_formation([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]))
print('-----1-------------')


def mineral_formation(stones):
    if 1 in stones[0] and 1 in stones[-1]:
        return "both"
    elif 1 in stones[0]:
        return "stalactites"
    elif 1 in stones[-1]:
        return "stalagmites"


print(mineral_formation([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]))

# Task 11


def pops(pop_list):
    if pop_list == [0]:
        return pop_list
    pivot_index = (len(pop_list)) // 2  # center
    pivot_value = pop_list[pivot_index]
    for i in range(1, pivot_value):
        pop_list[i] = i
        pop_list[pivot_value - i + pivot_value] = i
    return pop_list


print(pops(([0, 0, 0, 0, 4, 0, 0, 0, 0])))
print(pops(([0, 0, 0, 3, 0, 0, 0])))
print(pops(([0, 0, 2, 0, 0])))
print(pops(([0])))
print('------------------')


# Task 12 Intersecting Intervals
def count_overlapping(intervals, n):
    count = 0
    for interval in intervals:
        if (interval[0] <= n <= interval[1]):
            count += 1
        elif (interval[0] == n or interval[1] == n):
            count += 1
    return count


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))
print('------------------')

# Task 13 Tallest Skyscraper


def tallest_skyscraper(skyline):
    max_height = 0
    for col in range(len(skyline[0])):
        count = 0
        for row in range(len(skyline)):
            if skyline[row][col] == 1:
                count += 1
        if count > max_height:
            maxHeight = count
    return max_height


print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))
print('----------!--------')


# Task 15. Sharing is Caring
def show_the_love(share_list):
    smallest = min(share_list)
    total_removed = 0
    for i in range(len(share_list)):
        if share_list[i] != smallest:
            removed = share_list[i] * 1/4
            total_removed += removed
            share_list[i] = (share_list[i] - removed)
    share_list[share_list.index(smallest)] += total_removed
    return (share_list)


print(show_the_love([16, 10, 8]))
print('------------------')


# Task 6. Probabilities
def probability(numbers_list, n):
    # return '1' for every number >= n
    count = sum(1 for num in numbers_list if num >= n)
    # ', 1' округляє до десятків
    return round(100 * count / len(numbers_list), 1)


print(probability([7, 4, 17, 14, 12, 3], 16))
print('---------2---------')


# Task 14. Sum of Prime Numbers
def sum_primes(lst):
    if not lst:
        return None
    primes = []
    for number in lst:
        # ((number ** 0.5) + 1) функція інтерується через всі числа в даному діапазоні і перевіряє, чи ділиться вхідне число на будь-який з них. Якщо воно не ділиться на жодне з них, це означає, що вхідне число є простим числом.
        if number >= 2 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) and number <= 101:
            primes.append(number)
    return sum(primes)


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
