import sys
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def runcode(request):

    if request.method == 'POST':
        codeareadata = request.POST['codearea']

        try:
            # save original stdout ref.
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') # changing output to the file
            
            # execute code

            exec(codeareadata) # example =>print("Hello World!")
            sys.stdout.close()

            sys.stdout = original_stdout # resetting stdout to original value

            # reading output from the file and save in output variable
            output = open('file.txt', 'r').read()

        except Exception as e:
            # error handling
            sys.stdout = original_stdout
            output = e

    # finally return and render index page and send codedata and output to show
    # on page
    return render(request, 'index.html', {'code': codeareadata, 'output': \
        output})
