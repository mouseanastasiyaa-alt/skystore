from django.shortcuts import render


# Create your views here.
def home(request):
    """Контроллер главной страницы"""
    return render(request, "catalog/home.html")


def contacts(request):
    """Контроллер страницы контактов с обработкой формы обратной связи."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Здесь можно сохранить данные или отправить письмо
        print(f"Сообщение от {name} ({phone}): {message}")
        return render(request, "catalog/contacts.html", {
            "success": True,
            "name": name,
        })
    return render(request, "catalog/contacts.html")
