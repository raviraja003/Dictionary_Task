import datetime


def solution(D):
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    W = {}
    for st in week:
        W[st] = None

    for d, val in D.items():
        day = datetime.datetime.strptime(d, '%Y-%m-%d').strftime("%a")
        if W[day] == None:
            W[day] = 0

        W[day] += val

    p_one = 'Sun'
    p_two = 'Sat'

    for day, val in W.items():
        if W[day] == None:
            W[day] = 2 * W[p_one] - W[p_two]
        p_two = p_one
        p_one = day

    return W


if __name__ == '__main__':
    D = {'2020-01-01': 4, '2020-01-02': 4, '2020-01-03': 6, '2020-01-04': 8, '2020-01-05': 2, '2020-01-06': -6,
         '2020-01-07': 2, '2020-01-08': -2, }
    W = solution(D)
    print(W)
