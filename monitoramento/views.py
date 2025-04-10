from django.shortcuts import render

def index(request):
    cameras = [
        {"nome": "BOA VIAGEM", "channel": 1},
        {"nome": "GUARARAPES", "channel": 2},
        {"nome": "RUA DA AURORA", "channel": 3},
        {"nome": "DERBY", "channel": 4},
        {"nome": "AV. CONDE DA BOA VISTA", "channel": 5},
        {"nome": "BR-101", "channel": 6},
        {"nome": "PE-15", "channel": 7},
        {"nome": "TORRE AURORA", "channel": 8},
        {"nome": "CARUARU", "channel": 9},
    ]
    return render(request, 'index.html', {"cameras": cameras})
