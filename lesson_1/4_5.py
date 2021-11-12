def deposit(summ, time, money=0):
    deposit_small = {'begin_summ': 1000, 'end_summ': 10000, 6: 5, 12: 6, 24: 5}
    deposit_mid = {'begin_summ': 10000, 'end_summ': 100000, 6: 6, 12: 7, 24: 6.5}
    deposit_big = {'begin_summ': 100000, 'end_summ': 1000000, 6: 7, 8: 6, 24: 7.5}
    deposit_list = [deposit_small, deposit_mid, deposit_big]

    def add_money(deposit_type):
        nonlocal summ, time, money
        end_capitalization = 0
        end_money = 0
        # Рассчитываем процент на внесённую сумму помесячно, день внесения суммы не учитываем.
        for _el in range(time - 1):
            if _el > 0:
                capitalization = (end_money * deposit_type[time] / 12) / 100
                end_capitalization += capitalization
            end_money += money
        return end_money - money + end_capitalization

    for el in deposit_list:
        if el['begin_summ'] <= summ < el['end_summ']:
            if money != 0:
                return (summ + (summ * el[time] * time/12)/100) + add_money(el)
            return summ + (summ * el[time] * time/12)/100


print(deposit(1000, 6, 100))
