# MnasNet-pytorch-pretrained (Work in progress)

A pytorch pretrained model of MnasNet, paper: [MnasNet: Platform-Aware Neural Architecture Search for Mobile](https://arxiv.org/abs/1807.11626)

ref: https://github.com/AnjieZheng/MnasNet-PyTorch

## News

---------------------------12.Nov.2018 update---------------------------

Input size 299 trail has reached 70% top1 accuracy

| Top1 Accuracy | Top5 Accuracy |
| :------| :------ |
| 70.010 | 89.412 |


---------------------------09.Nov.2018 update---------------------------

I have tried with input size 299 and the accuracy is:

| Top1 Accuracy | Top5 Accuracy |
| :------| :------ |
| 69.880 | 89.438 |

Top1 Accuracy is quite close to 70%

## Introduction

The original paper says that on the ImageNet classification task, standard MnasNet Architecture achieves 74.0% top-1 accuracy with 76ms latency on a Pixel phone.

While I have tried many different training settings and pretrained it on standard ilsvrc12 Imagenet 1k training dataset(1281167 images) and tested the models on standard ilsvrc12 Imagenet 1k validation set(50000 images) with single-crop method, it achives (input_size = 224):

| Top1 Accuracy | Top5 Accuracy |
| :------| :------ |
| 68.964 | 88.730 |

You could refer to my logs for more details. Continuing my training process may achieve better results.

To the best of my knowledge, it is the highest Top1 Accuracy open-source model which only trained on standard ilsvrc12 Imagenet 1k training set(1281167 images) and test on validation set(50000 images).

## Training Strategies

Starting from lr 0.1, and decayed to its 0.5 every 20 epochs.

256 batchsize with 2 K80 GPU.

I tried with rmsprop as the paper says but it did not work well in my case, so I kept using SGD as my optimizer.

From the logs, we can see the model is underfitting, so I got rid of Dropout.

Image input size is crop to 224.

More details about crops and data augmentation methods could refer my codes.

## Quick start

1. Download data from Imagenet website.

2. Untar all zip files and use valprep.sh script to create validation set. If you would like to know more about this dataset, plz refer to this page: https://www.zhihu.com/question/273633408/answer/369134332

3. Simply run run_mnasnet.sh, you could continue my training by loading the pretrained model.

4. Use draw_log.py to parse the training log and draw plots after training done!

## Reference

If you feel it is useful about writing papers or any other materials by using this repo, please refer it as

```
@article{huwang2018mnasnet,
  title={mnasnet_pretrained https://github.com/billhhh/MnasNet-pytorch-pretrained},
  author={Hu Wang},
  year={2018}
}
```

Thank you!

## To-Do List

Some to-do list, you are welcome to have a try and see if it could have better accuracies and PR!

1. Shake-shake trick

2. Cutout trick (under trying)

3. Pretraine the model on imagenet 22k or tencent-ml-images(https://github.com/Tencent/tencent-ml-images), then fine-tune on ImageNet 1k

## Architecture

![Alt text](https://i.imgur.com/ryyU8cP.png)
