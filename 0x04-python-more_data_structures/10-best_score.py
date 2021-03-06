#!/usr/bin/python3
def best_score(a_dictionary):
    best = (None, 0)
    if a_dictionary:
        t_list = list(a_dictionary.items())
        for i in range(len(t_list)):
            if best[1] < t_list[i][1]:
                best = t_list[i]
        return best[0]
    return None


def main():
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))
    best_key = best_score(None)
    print("Best score: {}".format(best_key))


if __name__ == "__main__":
    main()
