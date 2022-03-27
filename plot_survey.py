import matplotlib.pyplot as plt
import numpy as np

def read_csv_lines(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split(',') for line in lines]
    return lines


def plot_age_distribution(lines):
  # Creating dataset
  ages_str = [line[0] for line in lines]
  lb1, lb2, lb3, lb4, lb5 = '10 - 20 anos', '21 - 30 anos', '31 - 40 anos', '41 - 50 anos', 'Mais de 50'
  age1, age2, age3, age4, age5 = ages_str.count(lb1), ages_str.count(lb2), ages_str.count(lb3), ages_str.count(lb4), ages_str.count(lb5)
  ages = [lb1, lb2, lb3, lb4, lb5]
  data = [age1, age2, age3, age4, age5]

  # Creating explode data
  explode = (0.1, 0.2, 0.1, 0.1, 0.1)

  # Creating colors parameters
  colors = ('#FF0000', '#FFA500', '#FFFF00', '#00FF00', '#0000FF')

  # Wedge properties
  wp = { 'linewidth' : 1, 'edgecolor' : "green" }

  # Creating autocpt arguments
  def func(pct, allvalues):
      absolute = int(pct / 100.*np.sum(allvalues))
      return '{:.1f}%({:.0f})'.format(pct, absolute)

  # Creating plot
  fig, ax = plt.subplots(figsize=(10, 7))
  wedges, texts, autotexts = ax.pie(data,
                                     wedgeprops=wp,
                                     colors=colors,
                                     autopct=lambda pct: func(pct, data),
                                     pctdistance=0.6,
                                     shadow=True,
                                     rotatelabels=True,
                                     explode=explode,
                                     textprops=dict(color="black", fontsize=6))

  for txt, pct_text in zip(texts, autotexts):
      pct_text.set_rotation(txt.get_rotation())

  ax.legend(wedges, ages, title='Idades', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

  plt.setp(autotexts, size=8, weight='bold')
  plt.show()


lines = read_csv_lines('survey_results.csv')
plot_age_distribution(lines)
