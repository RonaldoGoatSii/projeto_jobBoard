from django.shortcuts import render

def search_view(request):
    query = request.GET.get('q')
    print(query)  # só para testar
    return render(request, 'search/search.html')
