import matplotlib.pyplot as plt
import numpy as np
from pylab import *

# list_ddpg_10 = np.array([10.0, 13.0, 7.000000000000001, 7.000000000000001, 10.0, 4.0, 13.0, 10.0, 7.000000000000001, 11.0, 13.0, 12.0, 10.0, 19.0, 10.0, 12.0, 9.0, 12.0, 11.0, 12.0, 15.0, 8.0, 13.0, 6.0, 8.0, 10.0, 13.0, 10.0, 11.0, 10.0, 13.0, 9.0, 11.0, 13.0, 11.0, 9.0, 10.0, 11.0, 11.0, 15.0, 11.0, 8.0, 8.0, 18.0, 22.0, 9.0, 17.0, 10.0, 10.0, 9.0])
#
# list_ddpg_her_3 = np.array([5.0, 5.0, 12.0, 14.000000000000002, 30.0, 32.0, 32.0, 35.0, 34.0, 49.0, 45.0, 43.0, 39.0, 45.0, 50.0, 40.0, 47.0, 45.0, 57.99999999999999, 48.0, 48.0, 38.0, 45.0, 42.0, 50.0, 44.0, 55.00000000000001, 54.0, 48.0, 59.0, 71.0, 74.0, 78.0, 70.0, 77.0, 71.0, 81.0, 79.0, 74.0, 81.0, 78.0, 74.0, 82.0, 88.0, 81.0, 80.0, 77.0, 84.0, 85.0, 84.0])
# list_ddpg_her_5 = np.array([5.0, 7.000000000000001, 8.0, 7.000000000000001, 16.0, 35.0, 43.0, 33.0, 27.0, 46.0, 34.0, 46.0, 67.0, 69.0, 74.0, 77.0, 82.0, 88.0, 93.0, 95.0, 99.0, 99.0, 100.0, 98.0, 99.0, 100.0, 100.0, 99.0, 100.0, 99.0, 100.0, 99.0, 98.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.0])
# list_ddpg_her_10 = np.array([12.0, 10.0, 8.0, 8.0, 24.0, 49.0, 36.0, 43.0, 46.0, 48.0, 48.0, 52.0, 52.0, 49.0, 50.0, 54.0, 54.0, 50.0, 50.0, 46.0, 47.0, 44.0, 47.0, 51.0, 43.0, 52.0, 38.0, 49.0, 47.0, 18.0, 22.0, 23.0, 43.0, 62.0, 83.0, 89.0, 84.0, 80.0, 85.0, 81.0, 82.0, 75.0, 73.0, 72.0, 61.0, 57.99999999999999, 66.0, 73.0, 77.0, 96.0])
# list_ddpg_her_10_2 = np.array([6.0, 8.0, 6.0, 21.0, 15.0, 34.0, 37.0, 49.0, 66.0, 63.0, 66.0, 59.0, 68.0, 57.99999999999999, 80.0, 75.0, 64.0, 76.0, 81.0, 94.0, 98.0, 97.0, 96.0, 99.0, 98.0, 94.0, 98.0, 100.0, 98.0, 98.0, 99.0, 99.0, 100.0, 99.0, 100.0, 98.0, 100.0, 100.0, 100.0, 99.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# list_ddpg_her_20 = np.array([14.000000000000002, 11.0, 14.000000000000002, 13.0, 21.0, 27.0, 42.0, 43.0, 35.0, 62.0, 77.0, 82.0, 34.0, 33.0, 26.0, 54.0, 77.0, 86.0, 88.0, 92.0, 82.0, 83.0, 86.0, 93.0, 90.0, 91.0, 95.0, 97.0, 95.0, 88.0, 95.0, 92.0, 96.0, 92.0, 93.0, 91.0, 98.0, 92.0, 93.0, 94.0, 97.0, 98.0, 95.0, 97.0, 99.0, 98.0, 96.0, 95.0, 95.0, 89.0])
# list_ddpg_her_30 = np.array([18.0, 13.0, 21.0, 25.0, 22.0, 31.0, 18.0, 36.0, 25.0, 40.0, 56.00000000000001, 54.0, 30.0, 62.0, 69.0, 71.0, 56.00000000000001, 63.0, 86.0, 50.0, 38.0, 37.0, 37.0, 83.0, 91.0, 63.0, 64.0, 64.0, 72.0, 83.0, 83.0, 80.0, 93.0, 86.0, 91.0, 85.0, 82.0, 90.0, 77.0, 66.0, 80.0, 69.0, 80.0, 76.0, 82.0, 69.0, 94.0, 90.0, 81.0, 94.0])
#
# list_hierachical_ddpg_her_5 = np.array([8.0, 9.0, 5.0, 16.0, 34.0, 65.0, 48.0, 66.0, 50.0, 66.0, 69.0, 76.0, 63.0, 76.0, 82.0, 83.0, 88.0, 86.0, 88.0, 84.0, 83.0, 88.0, 97.0, 93.0, 94.0, 93.0, 99.0, 94.0, 97.0, 99.0, 94.0, 97.0, 98.0, 99.0, 100.0, 98.0, 100.0, 100.0, 99.0, 99.0, 100.0, 100.0, 96.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.0])
# list_hierachical_ddpg_her_10 = np.array([7.000000000000001, 7.000000000000001, 11.0, 16.0, 13.0, 11.0, 10.0, 17.0, 16.0, 17.0, 9.0, 10.0, 12.0, 21.0, 42.0, 26.0, 15.0, 14.000000000000002, 15.0, 16.0, 16.0, 38.0, 25.0, 20.0, 24.0, 40.0, 40.0, 14.000000000000002, 15.0, 5.0, 9.0, 17.0, 19.0, 21.0, 10.0, 13.0, 15.0, 9.0, 8.0, 13.0, 19.0, 25.0, 23.0, 19.0, 16.0, 23.0, 28.000000000000004, 24.0, 28.000000000000004, 25.0])
# list_hierachical_ddpg_her_3 = np.array([5.0, 8.0, 12.0, 9.0, 12.0, 6.0, 8.0, 30.0, 16.0, 32.0, 39.0, 44.0, 45.0, 50.0, 52.0, 54.0, 48.0, 59.0, 59.0, 51.0, 80.0, 67.0, 90.0, 97.0, 100.0, 99.0, 99.0, 99.0, 96.0, 99.0, 98.0, 100.0, 99.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# list_hierachical_ddpg_her_2 = np.array([8.0, 4.0, 7.000000000000001, 14.000000000000002, 13.0, 16.0, 21.0, 25.0, 23.0, 24.0, 23.0, 37.0, 31.0, 43.0, 34.0, 44.0, 45.0, 55.00000000000001, 49.0, 38.0, 56.00000000000001, 55.00000000000001, 48.0, 56.00000000000001, 56.00000000000001, 60.0, 54.0, 62.0, 56.00000000000001, 51.0, 62.0, 66.0, 67.0, 75.0, 90.0, 87.0, 93.0, 89.0, 92.0, 87.0, 77.0, 88.0, 85.0, 92.0, 96.0, 90.0, 94.0, 94.0, 95.0, 89.0])
#
# x = np.arange(0,5000, 100)
#
# plot(x, list_ddpg_10, label="DDPG")
#
# # plot(x,list_hierachical_ddpg_her_10, label="max_action = 10")
# plot(x,list_hierachical_ddpg_her_5, label="Hierachical DDPG + HER")
# # plot(x,list_hierachical_ddpg_her_3, label="max_action = 3")
# # plot(x,list_hierachical_ddpg_her_2, label="max_action = 2")
#
# # plot(x, list_ddpg_her_3, label="max_action = 3")
# # plot(x, list_ddpg_her_5, label="max_action = 5")
# plot(x, list_ddpg_her_10, label="DDPG + HER")
# plot(x, list_ddpg_her_20, label="max_action = 20")
# plot(x,list_ddpg_her_30, label="max_action = 30")
#
# path = "/Users/a/Desktop/毕设/reach环境数据/DDPG+RND/performance_data.txt"
# with open(path, "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         if line[0] in "0123456789":
#             num_list = [float(x) for x in line.split()]
#             plot(num_list)
#             plt.title("Performance")
#             plt.xlabel("Epoch")
#             plt.ylabel("Accuracy")
#             plt.savefig(path.replace(".txt", ".jpg"))
#
#         else:
#             continue
#


# # plt.title("DDPG + HER")
# plt.xlabel("Episode")
# plt.ylabel("Accuracy")
# plt.legend()
# plt.show()

def plot_data(path="performance_data.txt"):
    data_list = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line[0] in "0123456789":
                num_list = [float(x) for x in line.split()]
                data_list.append(num_list)
                # plot(num_list)
                # plt.title("Performance")
                # plt.xlabel("Epoch")
                # plt.ylabel("Accuracy")
                # plt.savefig(path.replace(".txt", ".jpg"))

            else:
                continue
    data_list_2 = [[] for _ in range(len(data_list[0]))]
    for i in range(len(data_list[0])):
        for j in range(len(data_list)):
            data_list_2[i].append(data_list[j][i])
    data_mean = [mean(x) for x in data_list_2]
    data_std = [sqrt(var(x)) for x in data_list_2]
    print(data_mean)
    print(data_std)
    x = range(len(data_list[0]))
    plot(x, data_mean)
    plt.fill_between(x, np.array(data_mean) - np.array(data_std), np.array(data_mean) + np.array(data_std), alpha=0.3)
    plt.title("Performance")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.savefig(path.replace(".txt", "_mean.jpg"))


def plot_list(path_list, label_list):
    for i, path in enumerate(path_list):
        data_list = []
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line[0] in "0123456789":
                    num_list = [float(x) for x in line.split()]
                    data_list.append(num_list)
                    # plot(num_list)
                    # plt.title("Performance")
                    # plt.xlabel("Epoch")
                    # plt.ylabel("Accuracy")
                    # plt.savefig(path.replace(".txt", ".jpg"))

                else:
                    continue
        data_list_2 = [[] for _ in range(len(data_list[0]))]
        for k in range(len(data_list[0])):
            for j in range(len(data_list)):
                data_list_2[k].append(data_list[j][k])

        data_mean = [mean(x) for x in data_list_2]
        data_std = [sqrt(var(x)) for x in data_list_2]
        print(data_mean)
        print(data_std)
        x = range(len(data_list[0]))
        plot(x, data_mean, label=label_list[i])
        plt.fill_between(x, np.array(data_mean) - np.array(data_std), np.array(data_mean) + np.array(data_std),
                         alpha=0.3)
    plt.title("Performance")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig("compare.jpg")




if __name__=="__main__":
    # path = "/Users/a/Desktop/毕设/reach环境数据/HDDPG2/50000episodes/performance_data.txt"
    # plot_data(path)

    path_list = ["/Users/a/Desktop/毕设/reach环境数据/DDPG+RND/performance_data_rnd_r0.txt","/Users/a/Desktop/毕设/reach环境数据/DDPG+RND/performance_data_rnd_r1.txt"]
    label_list = ["reward 0","reward 1"]
    plot_list(path_list, label_list)

    # plot_data()