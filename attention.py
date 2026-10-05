import numpy as np


def softmax(x):
    """
    Calculate softmax values.
    """
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def calculate_attention(embeddings):
    """
    Calculate scaled dot-product attention
    between the extracted text embeddings.
    """

    if embeddings is None or len(embeddings) == 0:
        return None

    X = np.asarray(embeddings, dtype=np.float32)

    # Query, Key, Value
    Q = X
    K = X
    V = X

    # Embedding dimension
    d_k = K.shape[1]

    # Scaled dot-product attention
    scores = np.matmul(Q, K.T) / np.sqrt(d_k)

    attention_weights = softmax(scores)

    # Attention output
    attention_output = np.matmul(
        attention_weights,
        V
    )

    # Overall importance of each text line
    importance_scores = np.mean(
        attention_weights,
        axis=0
    )

    return attention_weights, attention_output, importance_scores
