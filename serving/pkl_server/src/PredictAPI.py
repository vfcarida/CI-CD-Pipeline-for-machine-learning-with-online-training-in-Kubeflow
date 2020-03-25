import dill
import json
import os
import sys
import tarfile

from storage_util import download_blob

# https://stackoverflow.com/questions/42960637/python-3-5-dill-pickling-unpickling-on-different-servers-keyerror-classtype
dill._dill._reverse_typemap['ClassType'] = type

PKL_FILE_NAME='model.pkl'
CODE_FILE_NAME='model.tar.gz'

class PredictAPI(object):

  def __init__(self, pkl_path=None):
    print("pkl_path={}".format(pkl_path))

    download_blob(os.path.join(pkl_path, CODE_FILE_NAME), CODE_FILE_NAME)
    with tarfile.open(CODE_FILE_NAME, "r:gz") as tar:
      tar.extractall()

    download_blob(os.path.join(pkl_path, PKL_FILE_NAME), PKL_FILE_NAME)

    with open(PKL_FILE_NAME, 'rb') as model_file:
      self.model = dill.load(model_file)

  def predict_rest(self, X, names=None, meta=None):
    input_json = json.loads(X)
    input_str = input_json['strData']

    retval = self.model.predict_ranking(input_str)

    values = retval[0].tolist()
    return {'data':
            {'names': ['0','1'],
             'tensor':
             {'shape': [2],
              'values': values}}}

