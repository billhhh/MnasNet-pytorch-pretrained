#!/bin/bash
python wh_mnasnet_train.py --epochs 1000 --resume ./top1_68.3%_model_best.pth.tar ./ilsvrc12/
