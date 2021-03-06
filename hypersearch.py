import subprocess
import os

from train import main


seq_lens = [100, 1000, 4000]
layers = [1, 4, 8]
hidden_sizes = [100, 200, 400]

#for all combinations:

for seq_len in seq_lens:
    for layer in layers:
        for hidden_size in hidden_sizes:

            dir_name = "output/{}_{}_{}/".format(seq_len, layer, hidden_size)

            if not os.path.exists(dir_name):
                os.makedirs(dir_name)


            log = open(dir_name+'log.txt', 'a')
            print("Starting with hyperparams seq_len: {} layer: {} hidden_size: {}".format(seq_len, layer, hidden_size))

            main(directory='yamaha/tensors',n_epochs=1000,seq_len=seq_len,layers=layer,hidden_size=hidden_size, use_gpu=True)
