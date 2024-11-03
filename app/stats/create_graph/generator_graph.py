import matplotlib.pyplot as plt
import datetime

from app.utils import formating_subjects

async def date_sort(data):
    return sorted(data, key=lambda k: '.'.join((k['date'].split('.'))))


async def graph_generator(dict, subj, tg_id):
    dict = await date_sort(dict)
    x = []
    y = []

    for record in dict:
        if record['subject'] == subj:
            x.append(record['date'])
            y.append(record['resoult'])

    plt.clf()

    plt.bar(x, y, label='Балл', alpha=0.5)
    plt.plot(x, y, color='green', marker='o', markersize=7, alpha=0.8)
    plt.grid()
    plt.title(str(await formating_subjects(subj))[2:])
    plt.legend()
    plt.xticks(rotation=20)
    plt.savefig(f'plot_{datetime.date.today()}_{tg_id}.png', dpi=90)
    try:
        return str(round(sum(y)/len(y), 2))
    except ZeroDivisionError:
        return "0"