import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('3.csv', sep=';', header=None, names=['prep', 'group', 'grade'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

prep_grade_counts = df.groupby(['prep', 'grade']).size().unstack(fill_value=0)
prep_grade_counts.plot(kind='bar', stacked=True, ax=ax1, colormap='RdYlGn')
ax1.set_title('Распределение оценок по преподавателям')
ax1.set_xlabel('Преподаватель')
ax1.set_ylabel('Количество оценок')
ax1.legend(title='Оценка', bbox_to_anchor=(1, 1))

group_grade_counts = df.groupby(['group', 'grade']).size().unstack(fill_value=0)
group_grade_counts.plot(kind='bar', stacked=True, ax=ax2, colormap='RdYlGn')
ax2.set_title('Распределение оценок по группам')
ax2.set_xlabel('Группа')
ax2.set_ylabel('Количество оценок')
ax2.legend(title='Оценка', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('grades_distribution.png', dpi=200, bbox_inches='tight')
plt.show()