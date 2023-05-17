import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



### Plot alphas
data_path = '~/Desktop/PHD/Courses/NMS/Project/data/'
columns = ['churn', 'α = 2', 'α = 4', 'α = 6', 'α = 8', 'α = 10']
cmaps = ['b', 'g', 'r', 'c', 'y']

df100 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 100, k = 20).csv', usecols=columns)
df500 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 500, k = 20).csv', usecols=columns)
df1000 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 1000, k = 20).csv', usecols=columns)
dfs = [df100, df500, df1000]
labels = ['100', '500', '1000']

figall, axall = plt.subplots(2,3)

for i in range(len(dfs)):
    df = dfs[i]
    fig, ax = plt.subplots(1, 1)
    for j, cname in enumerate(columns[1:]):
        l1, = ax.plot(df.churn, df[cname], label=cname, color=cmaps[j])
        l1, = axall[0,i].plot(df.churn, df[cname], label=cname, color=cmaps[j])
    axall[0,i].set_ylim([0, 350])
    xticks = axall[0,i].get_xticks()[::3]
    axall[0,i].set_xticks(xticks)
    if(i>0):
        # axall[0,i].set_yticks([])
        axall[0,i].set_yticklabels([])
    
    ax.set_ylim([0, 350])
    ax.set_ylabel('Latency (ms)')
    ax.set_xlabel('churn rate')
    ax.legend(loc=2, ncol=2)
    ax.set_title(f'Latency under different churn rates; Network size {labels[i]}')
    fig.savefig(f'A_Latency_n{labels[i]}_fig.png')

df100 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 100, k = 20).csv', usecols=columns)
df500 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 500, k = 20).csv', usecols=columns)
df1000 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 1000, k = 20).csv', usecols=columns)
dfs = [df100, df500, df1000]

for i in range(len(dfs)):
    df = dfs[i]
    fig, ax = plt.subplots(1, 1)
    for j, cname in enumerate(columns[1:]):
        l1, = ax.plot(df.churn, df[cname], label=cname, color=cmaps[j])
        l1, = axall[1,i].plot(df.churn, df[cname], label=cname, color=cmaps[j])
    axall[1,i].set_ylim([0.5, 1.])
    axall[1,i].set_xlabel('churn rate')
    xticks = axall[1,i].get_xticks()[::3]
    axall[1,i].set_xticks(xticks)
    if(i>0):
        # axall[1,i].set_yticks([])
        axall[1,i].set_yticklabels([])
    
    ax.set_ylim([0.5, 1.1])
    ax.set_ylabel('Success rate')
    ax.set_xlabel('churn rate')
    ax.legend(loc=1, ncol=2)
    ax.set_title(f'Success rate under different churn rates; Network size {labels[i]}')
    fig.savefig(f'A_Success_n{labels[i]}_fig.png')

axall[0,0].set_ylabel('Latency (ms)')
axall[1,0].set_ylabel('Succes rate')
axall[1,0].legend(loc=3, labelspacing=0.3)#bbox_to_anchor=(0.5, 0.7))
for i in range(len(labels)):
    axall[0,i].set_title(f'Network size {labels[i]}')
figall.savefig(f'A_Latency-Success.pdf')

# # ################ in one figure
# # data_path = '~/Desktop/PHD/Courses/NMS/Project/data/'
# # columns = ['churn', 'α = 2', 'α = 4', 'α = 6', 'α = 8', 'α = 10']
# # cmaps = ['b', 'g', 'r', 'c', 'y']

# # df100 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 100, k = 20).csv', usecols=columns)
# # df500 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 500, k = 20).csv', usecols=columns)
# # df1000 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 1000, k = 20).csv', usecols=columns)

# # fig, ax = plt.subplots(1, 1)
# # ax2 = ax.twinx()
# # legend_linetypes = []
# # f1000_lines = []
# # for i, cname in enumerate(columns[1:]):
# #     l1, = ax.plot(df1000.churn, df1000[cname], label=cname, color=cmaps[i])
# #     l2, = ax.plot(df500.churn, df500[cname], '-.', color=cmaps[i])
# #     l3, = ax.plot(df100.churn, df100[cname], ':', color=cmaps[i])
# #     if(i == 0):
# #         l1, = ax2.plot(np.NaN, np.NaN, label='1000', color='black')
# #         l2, = ax2.plot(np.NaN, np.NaN, '-.', label='500', color='black')
# #         l3, = ax2.plot(np.NaN, np.NaN, ':', label='100', color='black')
# # ax2.get_yaxis().set_visible(False)
# # ax.set_ylim([0, 350])
# # ax.set_ylabel('Latency (ms)')
# # ax.set_xlabel('churn rate')
# # ax.legend(loc=2, ncol=2)
# # ax2.legend(loc=3, ncol=3)
# # ax.set_title('Latency under different churn rates')
# # fig.savefig('A_Latency_fig.png')

# # df100 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 100, k = 20).csv', usecols=columns)
# # df500 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 500, k = 20).csv', usecols=columns)
# # df1000 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 1000, k = 20).csv', usecols=columns)

# # fig, ax = plt.subplots(1, 1)
# # ax2 = ax.twinx()
# # legend_linetypes = []
# # f1000_lines = []
# # for i, cname in enumerate(columns[1:]):
# #     l1, = ax.plot(df1000.churn, df1000[cname], label=cname, color=cmaps[i])
# #     l2, = ax.plot(df500.churn, df500[cname], '-.', color=cmaps[i])
# #     l3, = ax.plot(df100.churn, df100[cname], ':', color=cmaps[i])
# #     if(i == 0):
# #         l1, = ax2.plot(np.NaN, np.NaN, label='1000', color='black')
# #         l2, = ax2.plot(np.NaN, np.NaN, '-.', label='500', color='black')
# #         l3, = ax2.plot(np.NaN, np.NaN, ':', label='100', color='black')
# # ax2.get_yaxis().set_visible(False)
# # ax.set_ylim([0.5, 1.1])
# # ax.set_ylabel('Success rate')
# # ax.set_xlabel('churn rate')
# # ax.legend(loc=2, ncol=2)
# # ax2.legend(loc=3, ncol=3)
# # ax.set_title('Success rate under different churn rates')
# # fig.savefig('A_Success_fig.png')



### Plot Ks
data_path = '~/Desktop/PHD/Courses/NMS/Project/data/'
columns = ['churn', 'k = 5', 'k = 10', 'k = 15', 'k = 20', 'k = 25', 'k = 30']
ks = [5, 10, 15, 20, 25, 30]
cmaps = ['b', 'g', 'r', 'c', 'y', 'm']

df100 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 100, alpha = 3).csv', usecols=columns)
df500 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 500, alpha = 3).csv', usecols=columns)
df1000 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 1000, alpha = 3).csv', usecols=columns)
dfs = [df100, df500, df1000]
labels = ['100', '500', '1000']

figall, axall = plt.subplots(2,3)
figslope, axslope = plt.subplots(1, 1)

for i in range(len(dfs)):
    df = dfs[i]
    fig, ax = plt.subplots(1, 1)
    slopes = np.zeros((len(ks)))
    assert(len(ks) == len(columns)-1)
    for j, cname in enumerate(columns[1:]):
        l1, = ax.plot(df.churn, df[cname], label=cname, color=cmaps[j])
        l1, = axall[0,i].plot(df.churn, df[cname], label=cname, color=cmaps[j])
        churn_float = [float(x.strip('%'))/100 for x in df.churn]
        slopes[j], _ = np.polyfit(churn_float, df[cname], 1)
    axall[0,i].set_ylim([0, 350])
    xticks = axall[0,i].get_xticks()[::3]
    axall[0,i].set_xticks(xticks)
    if(i>0):
        # axall[0,i].set_yticks([])
        axall[0,i].set_yticklabels([])

    axslope.plot(ks, slopes, label='N='+labels[i])
    
    ax.set_ylim([0, 350])
    ax.set_ylabel('Latency (ms)')
    ax.set_xlabel('churn rate')
    ax.legend(loc=2, ncol=2)
    ax.set_title(f'Latency under different churn rates; Network size {labels[i]}')
    fig.savefig(f'K_Latency_n{labels[i]}_fig.png')

axslope.legend()
axslope.set_title('Change of affects in k')
axslope.set_xlabel('k-bucket dimension')
axslope.set_ylabel('lin. reg. slope')
figslope.savefig('K_slope.pdf')


df100 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 100, alpha = 3).csv', usecols=columns)
df500 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 500, alpha = 3).csv', usecols=columns)
df1000 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 1000, alpha = 3).csv', usecols=columns)
dfs = [df100, df500, df1000]

for i in range(len(dfs)):
    df = dfs[i]
    fig, ax = plt.subplots(1, 1)
    for j, cname in enumerate(columns[1:]):
        l1, = ax.plot(df.churn, df[cname], label=cname, color=cmaps[j])
        l1, = axall[1,i].plot(df.churn, df[cname], label=cname, color=cmaps[j])
    axall[1,i].set_ylim([0.5, 1.])
    axall[1,i].set_xlabel('churn rate')
    xticks = axall[1,i].get_xticks()[::3]
    axall[1,i].set_xticks(xticks)
    if(i>0):
        # axall[1,i].set_yticks([])
        axall[1,i].set_yticklabels([])
    
    ax.set_ylim([0.5, 1.1])
    ax.set_ylabel('Success rate')
    ax.set_xlabel('churn rate')
    ax.legend(loc=1, ncol=2)
    ax.set_title(f'Success rate under different churn rates; Network size {labels[i]}')
    fig.savefig(f'K_Success_n{labels[i]}_fig.png')

axall[0,0].set_ylabel('Latency (ms)')
axall[1,0].set_ylabel('Succes rate')
axall[1,0].legend(loc=3, prop={'size':7}, labelspacing=0.3)#bbox_to_anchor=(0.5, 0.7))
for i in range(len(labels)):
    axall[0,i].set_title(f'Network size {labels[i]}')
figall.savefig(f'K_Latency-Success.pdf')



# ################ in one figure
# data_path = '~/Desktop/PHD/Courses/NMS/Project/data/'
# columns = ['churn', 'k = 5', 'k = 10', 'k = 15', 'k = 20', 'k = 25', 'k = 30']
# cmaps = ['b', 'g', 'r', 'c', 'y', 'm']

# df100 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 100, alpha = 3).csv', usecols=columns)
# df500 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 500, alpha = 3).csv', usecols=columns)
# df1000 = pd.read_csv(data_path + 'Kademlia Results - latency (n = 1000, alpha = 3).csv', usecols=columns)

# fig, ax = plt.subplots(1, 1)
# ax2 = ax.twinx()
# legend_linetypes = []
# f1000_lines = []
# for i, cname in enumerate(columns[1:]):
#     l1, = ax.plot(df1000.churn, df1000[cname], label=cname, color=cmaps[i])
#     l2, = ax.plot(df500.churn, df500[cname], '-.', color=cmaps[i])
#     l3, = ax.plot(df100.churn, df100[cname], ':', color=cmaps[i])
#     if(i == 0):
#         l1, = ax2.plot(np.NaN, np.NaN, label='1000', color='black')
#         l2, = ax2.plot(np.NaN, np.NaN, '-.', label='500', color='black')
#         l3, = ax2.plot(np.NaN, np.NaN, ':', label='100', color='black')
# ax2.get_yaxis().set_visible(False)
# ax.set_ylim([0, 350])
# ax.set_ylabel('Latency (ms)')
# ax.set_xlabel('churn rate')
# ax.legend(loc=2, ncol=2)
# ax2.legend(loc=3, ncol=3)
# ax.set_title('Latency under different churn rates')
# fig.savefig('K_Latency_fig.png')

# df100 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 100, alpha = 3).csv', usecols=columns)
# df500 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 500, alpha = 3).csv', usecols=columns)
# df1000 = pd.read_csv(data_path + 'Kademlia Results - Successful rate (n = 1000, alpha = 3).csv', usecols=columns)

# fig, ax = plt.subplots(1, 1)
# ax2 = ax.twinx()
# legend_linetypes = []
# f1000_lines = []
# for i, cname in enumerate(columns[1:]):
#     l1, = ax.plot(df1000.churn, df1000[cname], label=cname, color=cmaps[i])
#     l2, = ax.plot(df500.churn, df500[cname], '-.', color=cmaps[i])
#     l3, = ax.plot(df100.churn, df100[cname], ':', color=cmaps[i])
#     if(i == 0):
#         l1, = ax2.plot(np.NaN, np.NaN, label='1000', color='black')
#         l2, = ax2.plot(np.NaN, np.NaN, '-.', label='500', color='black')
#         l3, = ax2.plot(np.NaN, np.NaN, ':', label='100', color='black')
# ax2.get_yaxis().set_visible(False)
# ax.set_ylim([0.5, 1.1])
# ax.set_ylabel('Success rate')
# ax.set_xlabel('churn rate')
# ax.legend(loc=2, ncol=2)
# ax2.legend(loc=3, ncol=3)
# ax.set_title('Success rate under different churn rates')
# fig.savefig('K_Success_fig.png')




################
### Plot network size
data_path = '~/Desktop/PHD/Courses/NMS/Project/data/'
columns = ['churn', 'sz = 100', 'sz = 1000', 'sz = 10000']
cmaps = ['b', 'g', 'r', 'c', 'y', 'm']

df = pd.read_csv(data_path + 'Kademlia Results - latency (k = 20, alpha = 3).csv', usecols=columns)
labels = ['N=100', 'N=1000', 'N=10000']

fig, ax = plt.subplots(1, 1)
for j, cname in enumerate(columns[1:]):
    l1, = ax.plot(df.churn, df[cname], label=labels[j], color=cmaps[j])

ax.set_ylim([0, 350])
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('churn rate')
ax.legend(loc=2, ncol=2)
ax.set_title(f'under default configuration K = 20, α = 3')
fig.savefig(f'N_Latency_fig.pdf')

