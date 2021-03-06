
# Append to PYTHONPATH
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SVHNDigit.generic import train_model_from_images
from SVHNDigit.models.cnn import LeNet5Mod, HintonNet1, SermanetNet, CNN_B, InceptionNet

# Load SVHNDigit data

train_data_dir = 'data/imgs/train'
validation_data_dir = 'data/imgs/validation'

# Hyperparameters selected by tuning (LeNet5Mod)
lr = 0.01
reg_factor = 2e-5

# Hyperparameters selected by tuning (CNN_B)
# lr = 0.03
# reg_factor = 3e-6

decay = 0
dropout_param = 0.05
momentum = 0.9
# lr = 5e-2
# decay = 1e-3
# reg_factor = 1e-5
# dropout_param = 0.1
# momentum = 0.9

model_define_params = {'reg_factor': reg_factor,
                       'init': 'glorot_normal',
                       'use_dropout': False,
                       'dropout_param': dropout_param,
                       'use_batchnorm': True}

model_train_params = {'loss': 'categorical_crossentropy',
                      'optimizer': 'sgd',
                      'lr': lr,
                      'momentum': momentum,
                      'decay': decay,
                      'nesterov': True,
                      'metrics': ['accuracy'],
                      'batch_size': 128,
                      'nb_epochs': 20,
                      'nb_train_samples': 99712 * 6,
                      'nb_validation_samples': 6000}


input_dim = (3, 32, 32)
cnn = CNN_B(model_define_params, input_dim)
# cnn = LeNet5Mod(model_define_params, input_dim)
# cnn = InceptionNet(model_define_params, input_dim)
#cnn = SermanetNet(model_define_params, input_dim)
cnn.define(verbose=1)
history = train_model_from_images(cnn, model_train_params,
                                  train_data_dir, validation_data_dir,
                                  verbose=1, save_to_s3=False, early_stopping=False)
