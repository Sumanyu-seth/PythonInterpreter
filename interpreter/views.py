from django.shortcuts import render
import sys
import io

def code_interpreter(request):
    code_output = ""
    if request.method == "POST":
        code = request.POST.get("code")
        try:
            # Redirect stdout to capture print() output
            old_stdout = sys.stdout
            redirected_output = sys.stdout = io.StringIO()

            exec(code)  # Execute the user code

            sys.stdout = old_stdout
            code_output = redirected_output.getvalue()
        except Exception as e:
            code_output = str(e)

    return render(request, "index.html", {"output": code_output})
