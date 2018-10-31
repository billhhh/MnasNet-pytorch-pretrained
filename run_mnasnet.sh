#!/bin/bash
python wh_mnasnet_train.py --epochs 1000 --resume ./model_best.pth.tar ./ilsvrc12/
