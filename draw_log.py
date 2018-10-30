#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser("draw_log")
parser.add_argument('--f', type=str, default='log.out')

def main():
    global args
    args = parser.parse_args()
    file = open(args.f, 'r')
    init_epoch = -1
    epoch = -1
    x_train = []
    y_train_loss = []
    y_train_acc1 = []
    y_train_acc5 = []

    x_test = []
    y_test_loss = []
    y_test_acc1 = []
    y_test_acc5 = []

    while True:
        line = file.readline()
        if not line:
            break

        if line.find('Epoch: [')!=-1:
            # get all nums
            num_list = find_all_nums(line)
            epoch = int(num_list[0])
            batch = int(num_list[1])
            total_batch_epoch = int(num_list[2])
            if init_epoch == -1:
                init_epoch = epoch

            x_train.append(
                (epoch - init_epoch) * total_batch_epoch + batch
            )
            y_train_loss.append(float(num_list[7]))
            y_train_acc1.append(float(num_list[10]))
            y_train_acc5.append(float(num_list[13]))

        elif line.find('Test: [')!=-1:
            num_list = find_all_nums(line)
            batch = int(num_list[0])
            total_batch_epoch = int(num_list[1])

            x_test.append(
                (epoch - init_epoch) * total_batch_epoch + batch
            )
            y_test_loss.append(float(num_list[4]))
            y_test_acc1.append(float(num_list[7]))
            y_test_acc5.append(float(num_list[10]))

    draw_fig(x_train, y_train_loss, "Training Loss")
    draw_fig(x_train, y_train_acc1, "Training Top1 accuracy")
    draw_fig(x_train, y_train_acc5, "Training Top5 accuracy")

    draw_fig(x_test, y_test_loss, "Testing Loss")
    draw_fig(x_test, y_test_acc1, "Testing Top1 accuracy")
    draw_fig(x_test, y_test_acc5, "Testing Top5 accuracy")
    file.close()


# find all nums in a str
def find_all_nums(str):
    return re.findall(r"\d+\.?\d*", str)


def draw_fig(axis_x, axis_y, name):
    plt.cla()
    plt.plot(axis_x, axis_y, linewidth=1)
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.title(name)
    # plt.show()
    name += ".png"
    plt.savefig(name)

if __name__ == '__main__':
    main()