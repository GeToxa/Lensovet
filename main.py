import pandas as pd
from Text import text, Marka, name_of_spec



spt = text.split('title')
list_of_data = []
list_of_percents = []

final_ryad = []
final_mesto = []
final_cost = []
summ = 0
for i in spt:
    if i[2] == 's':
        pass
    else:
        list_of_data.append(i[2:70])
print(list_of_data)
list_of_data = list_of_data[1:]





for i in list_of_data:
    sp_i = i.split()
    print(sp_i)
    if Marka == 0:
        # Первый театр + лен совета смол
        ryad = sp_i[4]
        mesto = sp_i[6]
        cost = int(sp_i[8])
    else:
        # Ленсовета биг
        if sp_i[0] == 'Ложа':
            if sp_i[3] == 'огр.':
                sp_i.remove('огр.')
                sp_i.remove('вид')
                sp_i.remove('огр.')
                sp_i.remove('вид')
            cost = int(sp_i[8])
            ryad = sp_i[4]
            mesto = sp_i[6]

        elif sp_i[0] == 'Партер':
            if sp_i[4] == 'огр.':
                sp_i.remove('огр.')
                sp_i.remove('вид')
                sp_i.remove('огр.')
                sp_i.remove('вид')
            print('aaa', sp_i)
            cost = int(sp_i[9])
            ryad = sp_i[5]
            mesto = sp_i[7]

        else:
            cost = int(sp_i[9])
            ryad = sp_i[5]
            mesto = sp_i[7]

    final_ryad.append(ryad)
    final_mesto.append(mesto)
    final_cost.append(cost)

for i in final_cost:
    summ += i

List_of_new_cost = list(set(final_cost))
List_of_new_cost.sort()

uniq_sl = {"Характеристика":['Колличество мест','Общая стоимость мест']}
uniq_sl_p = {"Характеристика":['Колличество мест в %','Общая стоимость мест в %']}

for uniq_c in List_of_new_cost:
    uniq_summ = 0
    uniq_num = 0
    for cost in final_cost:
        if uniq_c == cost:
            uniq_num += 1
            uniq_summ += cost
    uno = [uniq_num, uniq_summ]
    unopers = [int((uniq_num/len(final_cost))*100), int((uniq_summ/summ)*100)]
    uniq_sl[uniq_c] = uno
    uniq_sl_p[uniq_c] = unopers

print(uniq_sl, '\n', uniq_sl_p)

df = pd.DataFrame({'Ряд': final_ryad,
                   'Место': final_mesto,
                   'Стоимость': final_cost})

ndf = pd.DataFrame(uniq_sl)

nndf = pd.DataFrame(uniq_sl_p)

what_to_write = {'Общая х-к': df, 'Кол-венная х-к' : ndf, 'Все в процентах' : nndf}

writer = pd.ExcelWriter(f'{name_of_spec}', engine='xlsxwriter')

for i in what_to_write:
    what_to_write[i].to_excel(writer, sheet_name=i)

writer.save()










