# Neural Variational Document Model (NVDM) tensorflow implementation

------

This is the tensorflow implementation of NVDM for the paper: 
[Neural Variational Inference for Text Processing][1]. Yishu Miao, Lei Yu, Phil Blunsom. ICML 2016.

Rewritten to run on arxiv dataset.

### Arxiv dataset
Please download and uncompress the [dataset][2] to: 
```
data/arxiv
```
### Train the Model

```
python nvdm.py --data_dir data/arxiv/
```
The script allows to specify the following parameters:
```
  --data_dir        Data dir path
  --learning_rate   Learning rate
  --batch_size      Batch size
  --n_hidden        Size of each hidden layer
  --n_topic         Size of stochastic vector
  --n_sample        Number of samples
  --vocab_size      Vocabulary size
  --test            Process test data
  --non_linearity   Non-linearity of the MLP
  --preprocessed    Wheather the test data was preprocessed
  
```

  [1]: https://arxiv.org/abs/1511.06038
  [2]: https://disk.yandex.ru/d/mF1Ho1NgKFNwQg?w=1
  [3]: https://arxiv.org/abs/1511.06038
