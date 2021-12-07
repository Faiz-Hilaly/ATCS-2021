#Faiz Hilaly
#12/7/2021

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("responses.csv")
#One obviously person's data was removed from the data
# set because it was obviously false.They claimed to
# average 2hrs of sleep per night during online learning.
# Data is below:
#11/19/2021 9:00:36,Sophomore,Same,8,2,In-person,In-person,3,7,7,7,Better now,Better now


#Variables
freshman = df[df["grade"] == "Freshman"]
sophomore = df[df["grade"] == "Sophomore"]
junior = df[df["grade"] == "Junior"]
senior = df[df["grade"] == "Senior"]


#Bar Chart - Sleep vs Grade vs State of School
labels = ['Freshmen', 'Sophomores', 'Juniors', 'All Students']
sleep_irl = [freshman["hrs_sleep_irl"].mean(),
             sophomore["hrs_sleep_irl"].mean(),
             junior["hrs_sleep_irl"].mean(),
             df["hrs_sleep_irl"].mean()]
sleep_online = [sophomore["hrs_sleep_dist"].mean(),
                junior["hrs_sleep_dist"].mean(),
                senior["hrs_sleep_dist"].mean(),
                df["hrs_sleep_dist"].mean()]

#margin of error is a 99% confidence t-interval
sleep_irl_margin_err = [freshman["hrs_sleep_irl"].sem() * 2.86093,
                        sophomore["hrs_sleep_irl"].sem() * 2.89823,
                        junior["hrs_sleep_irl"].sem() * 2.87844,
                        df["hrs_sleep_irl"].sem() * 2.62915]
sleep_online_margin_err = [sophomore["hrs_sleep_dist"].sem() * 2.89823,
                           junior["hrs_sleep_dist"].sem() * 2.87844,
                           senior["hrs_sleep_dist"].sem() *2.71541,
                           df["hrs_sleep_dist"].sem() * 2.62915]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sleep_online, width,
                yerr=sleep_online_margin_err, label='Distance')
rects2 = ax.bar(x + width/2, sleep_irl, width,
                yerr=sleep_irl_margin_err, label='In-person')

#label y axis
ax.set_ylabel('Average hours of sleep')
#title
ax.set_title('Sleep vs. Grade vs. State of School')
ax.set_xticks(x, labels)
#create legend
ax.legend()

#label bars with their values
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

#display graphic
fig.tight_layout()
plt.show()


#Bar Graph - HW Hours vs. Grade vs. State of School
labels = ['Freshmen', 'Sophomores', 'Juniors', 'All Students']
hw_irl = [freshman["hrs_hw_irl"].mean(),
          sophomore["hrs_hw_irl"].mean(),
          junior["hrs_hw_irl"].mean(),
          df["hrs_hw_irl"].mean()]
hw_online = [sophomore["hrs_hw_dist"].mean(),
             junior["hrs_hw_dist"].mean(),
             senior["hrs_hw_dist"].mean(),
             df["hrs_hw_dist"].mean()]

#margin of error is a 99% confidence t-interval
hw_irl_margin_err = [freshman["hrs_hw_irl"].sem() * 2.86093,
                     sophomore["hrs_hw_irl"].sem() * 2.89823,
                     junior["hrs_hw_irl"].sem() * 2.87844,
                     df["hrs_hw_irl"].sem() * 2.62915]
hw_online_margin_err = [sophomore["hrs_hw_dist"].sem() * 2.89823,
                        junior["hrs_hw_dist"].sem() * 2.87844,
                        senior["hrs_hw_dist"].sem() *2.71541,
                        df["hrs_hw_dist"].sem() * 2.62915]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects3 = ax.bar(x - width/2, hw_online, width,
                yerr=hw_online_margin_err, label='Distance')
rects4 = ax.bar(x + width/2, hw_irl, width,
                yerr=hw_irl_margin_err, label='In-person')

ax.set_ylabel('Average Hours Spent on Homework')
ax.set_title('HW Hours vs. Grade vs. State of School')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()
plt.show()


#Pie Chart - Respondent Grades
labels = ['Freshman', 'Sophomore', 'Junior', 'Senior']
sizes = [len(freshman), len(sophomore), len(junior), len(senior)]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

explode = (0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, colors=colors, labels=labels,
        autopct= lambda x:'{:.0f}'.format(int(round(x * len(df)/100))),
        startangle=90, pctdistance=0.85, explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()
plt.show()


#Bar Graph - Change in GPA
height = [len(df[df["gpa_change"] == 'Higher']),
          len(df[df["gpa_change"] == 'Lower']),
          len(df[df["gpa_change"] == 'Same'])]
bars = ('Higher', 'Lower', 'Same')
y_pos = np.arange(len(bars))

rect5 = plt.bar(y_pos, height)
plt.bar_label(rect5, padding=3)

plt.xticks(y_pos, bars)
plt.ylabel('Number of Students')
plt.title('Students vs. Change in GPA')
plt.ylim(0,50)

plt.show()


#Pie Chart - Learning Speed
labels = ['Online', 'In-person']
sizes = [len(df[df["learn_faster"] == 'Online']),
         len(df[df["learn_faster"] == 'In-person'])]

colors = ['#ff9999', '#66b3ff']

explode = (0.05, 0.05)

plt.pie(sizes, colors=colors, labels=labels,
        autopct= lambda x:'{:.0f}'.format(int(round(x * len(df)/100))),
        startangle=90, pctdistance=0.85, explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()
plt.show()


#Pie Chart - Mental Health
labels = ['Better online', 'Better In-person', 'The Same']
sizes = [len(df[df["mental_health"] == 'Better in quarantine']),
         len(df[df["mental_health"] == 'Better now']),
         len(df[df["mental_health"] == 'The same'])]

colors = ['#ff9999', '#66b3ff', '#99ff99']

explode = (0.05, 0.05, 0.05)

plt.pie(sizes, colors=colors, labels=labels,
        autopct= lambda x:'{:.0f}'.format(int(round(x * len(df)/100))),
        startangle=90, pctdistance=0.85, explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()
plt.show()


#Pie Chart - Physical Health
labels = ['Better online', 'Better In-person', 'The Same']
sizes = [len(df[df["physical_health"] == 'Better in quarantine']),
         len(df[df["physical_health"] == 'Better now']),
         len(df[df["physical_health"] == 'The same'])]

colors = ['#ff9999', '#66b3ff', '#99ff99']

explode = (0.05, 0.05, 0.05)

plt.pie(sizes, colors=colors, labels=labels,
        autopct= lambda x:'{:.0f}'.format(int(round(x * len(df)/100))),
        startangle=90, pctdistance=0.85, explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()
plt.show()

print(len(df[df["school_pref"] == 'In-person']))


#Bar Graph - Number of Classes vs. Grade vs. State of School
labels = ['5 Classes', '6 Classes', '7 Classes']
hw_irl = [len(df[df["num_classes_irl"] == 5]),
          len(df[df["num_classes_irl"] == 6]),
          len(df[df["num_classes_irl"] == 7])]
hw_online = [len(df[df["num_classes_dist"] == 5]),
             len(df[df["num_classes_dist"] == 6]),
             len(df[df["num_classes_dist"] == 7])]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects3 = ax.bar(x - width/2, hw_online, width, label='Distance')
rects4 = ax.bar(x + width/2, hw_irl, width, label='In-person')

ax.set_ylabel('Number of Students')
ax.set_title('Number of Students vs. Courseload')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()
plt.show()
