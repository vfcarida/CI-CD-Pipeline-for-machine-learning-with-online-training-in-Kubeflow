#!/bin/sh

# In a separate terminal, open a tunnel:
# kubectl port-forward svc/ambassador -n kubeflow 8080:80

STR_DATA=<<EOF
I have a normal form that sometimes return a file or redirects the user to another page. It's a report form where they can see results in PDF chart (page) Excel or HTML (page).   I don't have and I can't have a AJAX submission. I have only the following code:   <script type= text/javascript > \$('#myForm').submit(function(){ \$('.loading').fadeIn(); return; }); </script> <form id= myForm action= script.php > <input type= text name= first_name /> <input type= submit value= Submit /> <div class= loading >Loading...</div> </form>    This is a generic case to exemplify my actual code. What I want is to get the return of the form (in my case just the true return when it's a file download) to either remove the loading or place an error message.   Is that possible?
EOF

curl -v -g http://localhost:8080/seldon/sklearn-spacy-text-003/api/v0.1/predictions \
  -d '{"strData":"quero desbloquear meu cartao de debto"}'  -H "Content-Type: application/json"

