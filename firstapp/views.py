from django.shortcuts import render ,redirect
from docx import  *


arr = []
def index (request):
    if request.method == 'POST':
        file=str(request.FILES['document']).split()
        if("docx" in file)
          document = Document(file)
          lines = []
          for word in document.paragraphs:
             temp = ""
             sentence = (word.text).split()
             a = 0
             for x in sentence:
                if (x == ":"):
                    a = 1
                if (a > 1):
                    temp += x + " "
                a += 1
             lines.append(temp)
             for i in lines:
               arr.append(i)

          variable = {
                   'fname': arr[0],
                   'lname': arr[1],
                   'email': arr[2],
                   'number': arr[3],
                   'address': arr[4],
                   'city': arr[5],
                   'state': arr[6],
                   'country': arr[7],
                   'edu': arr[8],
                   'skill': arr[9],

          }
        return render(request, 'resume.html', variable)
      else:
        return redirect("wrongdoc/")
    return render(request, 'index.html')


