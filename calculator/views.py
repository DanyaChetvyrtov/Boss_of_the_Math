from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import MathematicalProblem, Answer


def mat_operations(request, number1, number2):
    if request.GET.get('add') == "":
        ans = number1 + number2

    elif request.GET.get('subtract') == "":
        ans = number1 - number2

    elif request.GET.get('multiply') == "":
        ans = number1 * number2

    else:
        ans = number1 / number2

    return ans


def index(request):
    return render(request, 'index.html')


def calc(request):
    return render(request, 'calc.html')


def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    ans = mat_operations(request, num1, num2)

    return render(request, 'result.html', {'ans': ans})


def matrix_calc(request):
    return render(request, 'matrix_calc.html')


def binary_calc(request):
    return render(request, 'binary_calc.html')


def binary_result(request):
    num1 = request.GET.get('bin_num1').strip()
    num2 = request.GET.get('bin_num2').strip()

    verif_1 = len([1 for x in num1 if x in '01']) == len(num1)
    verif_2 = len([1 for x in num2 if x in '01']) == len(num2)

    if not verif_1 or not verif_2:
        ans = 'Проверьте введённые данные'
        return render(request, 'binary_result.html', {'ans': ans})

    else:
        num1 = int(num1, 2)
        num2 = int(num2, 2)

        ans = bin(mat_operations(request, num1, num2))[2:]

        return render(request, 'binary_result.html', {'ans': ans})


class MathematicalProblemListView(generic.ListView):
    model = MathematicalProblem
    paginate_by = 5
