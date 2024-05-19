import torch


torch.manual_seed(0)


VAL_FRACTION = 0.3
TEST_FRACTION = 0.1

BATCH_SIZE = 128
EMB_SIZE = 512
NHEAD = 8
FFN_HID_DIM = 512
NUM_ENCODER_LAYERS = 3
NUM_DECODER_LAYERS = 3

LEARNING_RATE = 3e-4
NUM_EPOCHS = 10
