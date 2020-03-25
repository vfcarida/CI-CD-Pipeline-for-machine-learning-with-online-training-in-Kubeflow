"""Tests for ml_utils."""

import unittest
import ml_utils


class MlUtilsTest(unittest.TestCase):

  def test_clean_text(self):
    raw_html = """<p>I have a normal form that sometimes return a file or redirects the user to another page. It's a report form where they can see results in PDF chart (page) Excel or HTML (page).</p> <p>I don't have and I can't have a AJAX submission. I have only the following code:</p> <pre><code>&lt;script type= text/javascript &gt; $('#myForm').submit(function(){ $('.loading').fadeIn(); return; }); &lt;/script&gt; &lt;form id= myForm action= script.php &gt; &lt;input type= text name= first_name /&gt; &lt;input type= submit value= Submit /&gt; &lt;div class= loading &gt;Loading...&lt;/div&gt; &lt;/form&gt; </code></pre> <p>This is a generic case to exemplify my actual code. What I want is to get the return of the form (in my case just the true return when it's a file download) to either remove the loading or place an error message.</p> <p>Is that possible?</p>"""
    clean_html = """I have a normal form that sometimes return a file or redirects the user to another page. It's a report form where they can see results in PDF chart (page) Excel or HTML (page).   I don't have and I can't have a AJAX submission. I have only the following code:   <script type= text/javascript > $('#myForm').submit(function(){ $('.loading').fadeIn(); return; }); </script> <form id= myForm action= script.php > <input type= text name= first_name /> <input type= submit value= Submit /> <div class= loading >Loading...</div> </form>    This is a generic case to exemplify my actual code. What I want is to get the return of the form (in my case just the true return when it's a file download) to either remove the loading or place an error message.   Is that possible?"""
    retval = ml_utils.CleanTextTransformer.transform_clean_text(raw_html)
    print(retval)


if __name__ == '__main__':
  unittest.main()
