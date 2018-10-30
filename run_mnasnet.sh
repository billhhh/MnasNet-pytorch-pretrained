#!/bin/bash
python wh_mnasnet_train.py --epochs 1000 --resume ./checkpoint.pth.tar ./ilsvrc12/
