import matplotlib.pyplot as plt
import numpy as np


def read_csv_lines(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split(',') for line in lines]
    return lines


def create_age_dataset(lines):
  print('Creating age dataset...')
  # Creating dataset
  ages_str = [line[0] for line in lines]
  lb1, lb2, lb3, lb4, lb5 = '10 - 20 anos', '21 - 30 anos', '31 - 40 anos', '41 - 50 anos', 'Mais de 50'
  ageCount1, ageCount2, ageCount3, ageCount4, ageCount5 = ages_str.count(lb1), ages_str.count(lb2), ages_str.count(lb3), ages_str.count(lb4), ages_str.count(lb5)
  labels = [lb1, lb2, lb3, lb4, lb5]
  data = [float(ageCount1), float(ageCount2), float(ageCount3), float(ageCount4), float(ageCount5)]  
  return dict(zip(labels, data))

# Plot age distribution in a histogram received from a dictionary where the keys are the labels and the values are the data
def plot_age_distribution_in_histogram(ages_freq):
  print('Creating age distribution...')
  labels = list(ages_freq.keys())
  data = list(ages_freq.values())

  # Creating plot
  fig, ax = plt.subplots(figsize=(10, 7))
  ax.bar(labels, data, color='#BD472E', width=0.5)
  ax.set_title('Distribuição de idades')
  ax.set_xlabel('Idades')
  ax.set_ylabel('Frequencia')
  print('Saving age distribution in histogram...')
  plt.savefig('plots/age_distribution_hist.png', bbox_inches='tight')


def plot_age_distribution_in_pie_chart(ages_freq):
  print('Creating age distribution...')
  labels = list(ages_freq.keys())
  data = list(ages_freq.values())

  # Creating explode data
  explode = (0.01, 0.1, 0.01, 0.01, 0.01)

  # Creating colors parameters
  colors = ('#A1BD2E', '#BD472E', '#2EA4BD', '#41949D', '#4CB43F')

  # Wedge properties
  wp = { 'linewidth' : 1, 'edgecolor' : "white" }

  # Creating autocpt arguments
  def func(pct, allvalues):
      absolute = int(pct / 100 * sum(allvalues))
      if absolute == 80:
        absolute+=1
      return '{:.2f}%({:.0f})'.format(pct, absolute)

  # Creating plot
  fig, ax = plt.subplots(figsize=(10, 7))
  wedges, texts, autotexts = ax.pie(data,
                                     wedgeprops=wp,
                                     colors=colors,
                                     autopct=lambda pct: func(pct, data),
                                     pctdistance=0.7,
                                     rotatelabels=True,
                                     explode=explode,
                                     textprops=dict(color="black", fontsize=11))

  for txt, pct_text in zip(texts, autotexts):
      pct_text.set_rotation(txt.get_rotation())

  ax.legend(wedges, labels, title='Idades', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
  ax.set_title('Distribuição de idades')
  print('Saving age distribution in pie chart...')
  plt.savefig('plots/age_distribution_pie.png', bbox_inches='tight')  


def process_social_networks(lines):
  print('Processing social networks...')
   # Creating dataset
  sn_str = [line[1] for line in lines]
  sn_count = {}
  for sn in sn_str[1:]:
    sns_splited = sn.split(';')
    for sn_splited in sns_splited:
      sn_splited = sn_splited.lower().strip()
      if sn_splited in sn_count:
        sn_count[sn_splited] += 1
      else:
        sn_count[sn_splited] = 1
  return sn_count
 
# Plot social networks distribution in a histogram received from a dictionary where the keys are the labels and the values are the data
def plot_social_networks_distribution_in_histogram(social_networks_freq):
  print('Creating social networks distribution...')
  labels = list(social_networks_freq.keys())
  data = list(social_networks_freq.values())

  # Creating plot
  fig, ax = plt.subplots(figsize=(10, 7))
  ax.bar(labels, data, color='#A1BD2E', width=0.5)
  ax.set_title('Distribuição de redes sociais')
  ax.set_xlabel('Redes sociais')
  ax.set_ylabel('Frequencia')
  plt.savefig('plots/social_networks_distribution_hist.png', bbox_inches='tight')


lines = read_csv_lines('data/survey_results.csv')

# Ages frequency
ages_frequency = create_age_dataset(lines[1:])
plot_age_distribution_in_histogram(ages_frequency)
plot_age_distribution_in_pie_chart(ages_frequency)

# Social networks frequency
sn_frequency = process_social_networks(lines)
plot_social_networks_distribution_in_histogram(sn_frequency)
