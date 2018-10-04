"""
    A policy gradient agent with convolutional neural network.

    More Info : https://github.com/mlitb/pong-cnn
    Authors:
        1. Faza Fahleraz https://github.com/ffahleraz
        2. Nicholas Rianto Putra https://github.com/nicholaz99
        3. Abram Perdanaputra https://github.com/abrampers
"""

import gym
import numpy as np
import tensorflow as tf
from typing import Tuple


class Agent:

    def __init__(self, input_shape: Tuple[int, int, int]):
        self.conv1 = tf.keras.layers.Conv2D(input_shape=input_shape, filters=16, 
                kernel_size=8, strides=4, activation='relu', data_format="channels_last")
        self.conv2 = tf.keras.layers.Conv2D(filters=32, kernel_size=4, strides=2, 
                activation='relu')
        self.flatten = tf.keras.layers.Flatten()
        self.fc = tf.keras.layers.Dense(256, activation='relu')
        self.prob = tf.keras.layers.Dense(1, activation='sigmoid')


    def _forward_pass(self, state: tf.Tensor) -> tf.Tensor:
        """Compute the probability distribution of actions according to the policy."""
        l1 = self.conv1(state)
        l2 = self.conv2(l1)
        l3 = self.flatten(l2)
        l4 = self.fc(l3)
        l5 = self.prob(l4)
        return l5


    def sample_action(self, state: tf.Tensor) -> tf.Tensor:
        """Sample action according to the policy from a given state."""
        prob = self._forward_pass(state)
        return 2 if np.random.uniform() < prob[0][0] else 5


    def update(self, reward: float, reset_value: bool, reset_episode: bool):
        pass


    def update_policy(self):
        pass
