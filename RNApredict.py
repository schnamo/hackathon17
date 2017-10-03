#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Model training for Distraction data set using Validation Monitor."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import os
import tempfile

import tensorflow as tf
import numpy as np

# Data sets
target_col = 36
model_dir = "128x64rnainteract{}".format(target_col)
os.system("mkdir "+model_dir)


def main(argv):
  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=argv[1],
    target_dtype=np.int,
    target_column=target_col,
    features_dtype=np.float32)
  test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=argv[2],
    target_dtype=np.int,
    target_column=target_col,
    features_dtype=np.float32)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=36)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[128,64],
                                            n_classes=2,
                                            #optimizer=tf.train.AdamOptimizer(learning_rate=0.05),
					    dropout=0.8,
                                            model_dir=model_dir)

  # Fit model.
  if argv[3] != "test":
     classifier.fit(x=training_set.data,
               y=training_set.target,
               steps=10000)

     # Evaluate accuracy.
     accuracy_score = classifier.evaluate(x=test_set.data,
                                     y=test_set.target)["accuracy"]
     print('Accuracy: {0:f}'.format(accuracy_score))

  else:
     # Classify new test samples.
     y = list(classifier.predict(test_set.data, as_iterable=True))
     for pred in y:
       print('{}'.format(str(pred)))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.register("type", "bool", lambda v: v.lower() == "true")
  parser.add_argument(
      "--train_data", type=str, default="", help="Path to the training data.")
  parser.add_argument(
      "--test_data", type=str, default="", help="Path to the test data.")
  parser.add_argument(
      "--predict_data",
      type=str,
      default="",
      help="Path to the prediction data.")
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

