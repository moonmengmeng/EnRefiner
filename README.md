# EnRefiner

## Dependency
Pytorch 1.7.1
tensorboard 2.4.1
transformers 4.6.1
tree-sitter 0.2.2

## Download
CodeT5 Pre-trained checkpoints: https://console.cloud.google.com/storage/browser/sfr-codet5-data-research/pretrained_models

## Train prompt-augmented model A

cd prompt_augmented_A\sh

python run_exp.py --model_tag codet5_base --task translate --sub_task java-cs

**NOTE: modify WORKDIR in exp_with_args.sh**

## Train prompt-augmented model B

cd prompt_augmented_B\sh

python run_exp.py --model_tag codet5_base --task translate --sub_task java-cs

**NOTE: modify WORKDIR in exp_with_args.sh**

## Train retrieval-augmented model

cd retrieval_augmented\sh

python run_exp.py --model_tag codet5_base --task translate --sub_task java-cs

**NOTE: modify WORKDIR in exp_with_args.sh**

## Ensemble

use vote.py in dir **output**
