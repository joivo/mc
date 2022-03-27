# social network analysis distribution
# social_networks = [line[1] for line in lines]

# lb1, lb2, lb3, lb4, lb5 = 'Instagram', 'Twitter', '31 - 40 anos', '41 - 50 anos', 'Mais de 50'
# age1, age2, age3, age4, age5 = social_networks.count(lb1.to), social_networks.count(lb2), social_networks.count(lb3), social_networks.count(lb4), social_networks.count(lb5)

# labels = [lb1, lb2, lb3, lb4, lb5]
# data = [age1, age2, age3, age4, age5]

# fig1, ax1 = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

# def func(pct):    
#     return "{:.1f}%".format(pct)


# wedges, texts, autotexts = ax1.pie(data, autopct=lambda pct: func(pct), pctdistance= 0.5, startangle=90, rotatelabels=True,
#                                     textprops=dict(color="w"))

# for txt, pct_text in zip(texts, autotexts):
#     pct_text.set_rotation(txt.get_rotation())

# ax1.legend(wedges, labels, title='Idades por intervalos', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# plt.setp(autotexts, size=8, weight='bold')
# plt.show()


# # social network for job
# job_purpose = [line[2] for line in lines]

# # average usage of social network per week
# average_usage_per_week = [line[3] for line in lines]

# # no social network usage belief
# no_social_network_usage = [line[4] for line in lines]

# # no social network usage time
# no_social_network_usage_time = [line[5] for line in lines]

# # feels anxious about social network usage
# feels_anxious = [line[6] for line in lines]

# # fomo identification
# fomo_identification = [line[7] for line in lines]

# # social network usage causing damage belief
# damage_belief = [line[8] for line in lines]

# # task with focus required
# task_focus_required = [line[9] for line in lines]

# # lost attention because social network usage
# lost_attention = [line[10] for line in lines]

# # focus time on a sigle task
# focus_time = [line[11] for line in lines]

# # impact for make things done
# things_done = [line[12] for line in lines]

# # context switching cost
# context_switch_cost = [line[13] for line in lines]

# # task frustration
# task_frustration = [line[14] for line in lines]

# # still use pomodoro technique
# still_use_pomo = [line[15] for line in lines]

# # use pomodoro technique some time
# already_use_pomo = [line[16] for line in lines]
