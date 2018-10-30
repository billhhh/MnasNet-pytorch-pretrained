# MnasNet-pytorch-pretrained

A pytorch pretrained model for MnasNet, paper: [MnasNet: Platform-Aware Neural Architecture Search for Mobile](https://arxiv.org/abs/1807.11626)

ref: https://github.com/AnjieZheng/MnasNet-PyTorch

## Introduction

The original paper said on the ImageNet classification task, standard MnasNet Architecture achieves 74.0% top-1 accuracy with 76ms latency on a Pixel phone.

I tried many different settings and pretrained it on standard ilsvrc12 Imagenet 1k trainging dataset(1281167 training images) and validation set(50000 validation images) with single-crop method, it achives:


| Top1 Accuracy | Top5 Accuracy |
| :------| :------ |
| 68.300 | 88.364 |

You could refer log for more details. Continuing training maybe get better results

To the best of my knowledge, it is the highest Top1 Accuracy which only trained on standard ilsvrc12 Imagenet 1k dataset and test on validation set(50000 validation images).

## Training Strategies

Starting from defualt lr which is 0.1, and decayed to its 0.5 every 20 epochs.

256 batchsize with 2 K80 GPU.

I tried with rmsprop but it seems cannot achieve good result in my case, so I kept using SGD as my optimizer.

More details about crops and data augmentation methods could refer the codes.

## Quick start

1. Download data from Imagenet website.

2. Untar all the zip files and use valprep.sh script to create validation set. If you want to know more about this dataset, plz refer this page: https://www.zhihu.com/question/273633408/answer/369134332

3. Simply run run_mnasnet.sh, you could continue training by loading the pretrained model.

4. Use draw_log.py to parse log and draw plots after training done!

## Reference

If you feel it is useful and writing papers or any other materials by using this repo, please refer it as

```
@article{huwang2018mnasnet,
  title={mnasnet_pretrained},
  author={Hu Wang},
  year={2018}
}
```

Thank you!

## To-Do List

Some to-do list, you guys are welcome to have a try and see if it could have better accuracies!

1. shake-shake trick

2. cutout trick

3. pretrained on imagenet 22k or tencent-ml-images(https://github.com/Tencent/tencent-ml-images)

## Architecture

![Alt text](https://i.imgur.com/ryyU8cP.png)
