def my_fact_rec(a):
    if a < 2:
        return 2
    return a * my_fact_rec(a - 1)


if __name__ == '__main__':
    a = 4
    a = my_fact_rec(a)

    print("Oof fact {0}".format(a))



