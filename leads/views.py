from django.http import JsonResponse

def leads(request):
    if request.method == 'GET':
        lead = {
            'id': '1',
            'nome': 'Gabriel'
        }
        return JsonResponse(lead)