# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def quadratic_results(request):
    numbers = {'a' : [request.GET['a'], ''],
               'b' : [request.GET['b'], ''],
               'c' : [request.GET['c'], '']
                }

    for key in numbers:
        if numbers[key][0] == '':
            numbers[key][1] = 'коэффициент не определен'
        else:
            try:
                int(numbers[key][0])
            except Exception:
                numbers[key][1] = 'коэффициент не целое число'
                continue
            if key == 'a' and int(numbers['a'][0]) == 0:
                numbers['a'][1] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if ''.join([numbers[key][1] for key in numbers]) == '':
        a = float(numbers['a'][0])
        b = float(numbers['b'][0])
        c = float(numbers['c'][0])
        d = (b*b)-(4*a*c)
        if d>0:
            x1 = (-b+((b*b-4*a*c)**(1/2.0)))/2*a
            x2 = (-b-((b*b-4*a*c)**(1/2.0)))/2*a
            dk = 'Дискриминант: %.0f' % d
            message = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f x2 = %.1f' % (x1, x2)
            discr = {'d' : [dk,message]}
        elif d==0:
            x = -float(b)/(2*float(a))
            dk = 'Дискриминант: 0'
            message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
            discr = {'d' : [dk,message]}
        else:
            dk = 'Дискриминант: %.0f' % d
            message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            discr = {'d' : [dk,message]}
        numbers.update(discr)

    return render(request, 'results.html', numbers)
