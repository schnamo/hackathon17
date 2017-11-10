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
import pandas as pd
import itertools

import config

# Data sets
target_col = config.target_col
model_dir = config.model_dir+sys.argv[4]
if os.access(model_dir, os.R_OK) != True:
   os.mkdir(model_dir)

FEATURES = [ "p1","p2","p3","p4","p5","p6","p7","m1","m2","m3","m4","p11","p12","p13","p14","p15","p16","p17","p21","p22","p23","p24","p25","p26","p27","m11","m12","m13","m14","p31","p32","p33","p34","p35","p36","p37" ]
COLUMNS = [ "p1","p2","p3","p4","p5","p6","p7","m1","m2","m3","m4","p11","p12","p13","p14","p15","p16","p17","p21","p22","p23","p24","p25","p26","p27","m11","m12","m13","m14","p31","p32","p33","p34","p35","p36","p37","label" ]
LABEL = "label"

def input_fn(data_set):
  feature_cols = {k: tf.constant(data_set[k].values) for k in FEATURES}
  labels = tf.constant(data_set[LABEL].values)
  return feature_cols, labels


def main(argv):


  # Load datasets
  #training_set = pd.read_csv(argv[1], skipinitialspace=True, header=None, skiprows=0, names=COLUMNS)

  #test_set = pd.read_csv(argv[2], skipinitialspace=True, header=None, skiprows=0, names=COLUMNS)

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
  #feature_columns = [tf.contrib.layers.real_valued_column(k) for k in FEATURES]
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=config.dimensions)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=config.hidden_units,
                                            n_classes=2,
                                            #optimizer=tf.train.AdamOptimizer(learning_rate=0.05),
					    dropout=0.8,
                                            model_dir=model_dir)
  

  # Fit model.
  if argv[3] == "learn":
     #train_input_fn = tf.estimator.inputs.numpy_input_fn(
     #   x={"x": np.array(training_set.data)}, y=np.array(training_set.target), batch_size=64, shuffle=True, num_epochs=None)
     #train_input_fn = tf.estimator.inputs.pandas_input_fn(
     #   x=pd.DataFrame({k: training_set[k].values for k in FEATURES}), y=pd.Series(training_set[LABEL].values), shuffle=True, num_epochs=None)

     #classifier.fit(input_fn=train_input_fn, steps=config.steps)
     #classifier.fit(input_fn=lambda: input_fn(training_set), steps=1) #config.steps)
     classifier.fit(x=training_set.data, y=training_set.target, steps=config.steps)

     # Evaluate accuracy.
     #test_input_fn = tf.estimator.inputs.numpy_input_fn(
     #   x={"x": np.array(test_set.data)}, y=np.array(test_set.target), batch_size=64, shuffle=True, num_epochs=None)
     #test_input_fn = tf.estimator.inputs.pandas_input_fn(
     #   x=pd.DataFrame({k: test_set[k].values for k in FEATURES}), y=pd.Series(test_set[LABEL].values), shuffle=False, num_epochs=1)

     #accuracy_score = classifier.evaluate(input_fn=test_input_fn, steps=1)["accuracy"]
     accuracy_score = classifier.evaluate(x=test_set.data, y=test_set.target)["accuracy"]
     #accuracy_score = classifier.evaluate(input_fn=lambda: input_fn(test_set))["accuracy"]
     print('Accuracy: {0:f}'.format(accuracy_score))

  if argv[3] == "test":
     # Evaluate accuracy.
     #test_input_fn = tf.estimator.inputs.numpy_input_fn(
     #   x={"x": np.array(test_set.data)}, y=np.array(test_set.target), batch_size=64, shuffle=True, num_epochs=None)

     #test_input_fn = tf.estimator.inputs.pandas_input_fn(
     #   x=pd.DataFrame({k: test_set[k].values for k in FEATURES}), y=pd.Series(test_set[LABEL].values), shuffle=False, num_epochs=1)

     #accuracy_score = classifier.evaluate(input_fn=test_input_fn, steps=1)["accuracy"]
     #accuracy_score = classifier.evaluate(input_fn=lambda: input_fn(test_set))["accuracy"]
     accuracy_score = classifier.evaluate(x=test_set.data, y=test_set.target)["accuracy"]
     print('Accuracy: {0:f}'.format(accuracy_score))

  if argv[3] == "pred":
     # Classify new test samples.
     #test_input_fn = tf.estimator.inputs.numpy_input_fn(
     #   x={"x": np.array(test_set.data)}, y=None, batch_size=64, shuffle=True, num_epochs=None)
     #test_input_fn = tf.estimator.inputs.pandas_input_fn(
     #   x=pd.DataFrame({k: test_set[k].values for k in FEATURES}), y=pd.Series(test_set[LABEL].values), shuffle=False, num_epochs=1)

     y = list(classifier.predict(test_set.data, as_iterable=True))
     #y = classifier.predict(input_fn=test_input_fn) #, as_iterable=True)
     #y = list(classifier.predict(input_fn=lambda: input_fn(test_set), as_iterable=True))
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

