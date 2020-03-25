"""Tests for trainer."""

import unittest

import trainer

import dill

TRAIN_FILE_NAME = 'train.csv'
PKL_FILE_NAME = 'model.pkl'

class TrainerTest(unittest.TestCase):

  def setUp(self):

    self.model = trainer.preprocess_and_train(train_data=TRAIN_FILE_NAME,
                         eval_data=TRAIN_FILE_NAME,
                         output=PKL_FILE_NAME)

  def test_predict(self):
    input_str = """<p>I have a normal form that sometimes return a file or redirects the user to another page. It's a report form where they can see results in PDF chart (page) Excel or HTML (page).</p> <p>I don't have and I can't have a AJAX submission. I have only the following code:</p> <pre><code>&lt;script type= text/javascript &gt; $('#myForm').submit(function(){ $('.loading').fadeIn(); return; }); &lt;/script&gt; &lt;form id= myForm action= script.php &gt; &lt;input type= text name= first_name /&gt; &lt;input type= submit value= Submit /&gt; &lt;div class= loading &gt;Loading...&lt;/div&gt; &lt;/form&gt; </code></pre> <p>This is a generic case to exemplify my actual code. What I want is to get the return of the form (in my case just the true return when it's a file download) to either remove the loading or place an error message.</p> <p>Is that possible?</p>"""
    # input_str = "This is a test input 6"
    retval = self.model.predict_ranking(input_str, top=5)
    print(retval)


if __name__ == '__main__':
  unittest.main()
