class Config:
    READ_RESPONSE = False
    INPUT = "command"  # voice, command

    USE_MODEL = True
    PRETRAINED = True
    PRETRAINED_EMBEDDING = "embeddings/sgns.weibo.bigram"
    CUDA = False
    DEVICE = 0

    EMOTION_MODEL = "SVM"  # SVM, CNN, LSTM, MLP
    GET_RADAR = False  # False, True
    TRAIN = False  # False, True
