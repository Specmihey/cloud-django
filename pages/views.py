from django.shortcuts import render

# Отображение страниц приложения
#request - запрос, "home.html" - имя шаблона, {} - пока пропустим
def home(request):
	return render(request, "home.html", {})

def about(request):
	my_name = "Hello, My Name Is John Elder!"
	return render(request, "about.html", {"my_name": my_name})

def contact(request):
	from pages.namer import bob
	return render(request, "contact.html", {"my_stuff": bob})