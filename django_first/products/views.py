from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductLine

# READ – List all product lines
def productline_list(request):
    productlines = ProductLine.objects.all()
    return render(request, "products/productline_list.html", {"productlines": productlines})

# CREATE – Add product line
def productline_create(request):
    if request.method == "POST":
        ProductLine.objects.create(
            productLine=request.POST["productLine"],
            textDescription=request.POST.get("textDescription"),
            htmlDescription=request.POST.get("htmlDescription"),
        )
        return redirect("productline_list")

    return render(request, "products/productline_form.html")

# UPDATE – Edit an existing product line
def productline_update(request, pk):
    pl = get_object_or_404(ProductLine, pk=pk)

    if request.method == "POST":
        pl.textDescription = request.POST.get("textDescription")
        pl.htmlDescription = request.POST.get("htmlDescription")
        pl.save()
        return redirect("productline_list")

    return render(request, "products/productline_form.html", {"productline": pl})

# DELETE – Delete a product line
def productline_delete(request, pk):
    pl = get_object_or_404(ProductLine, pk=pk)
    if request.method == "POST":
        pl.delete()
        return redirect("productline_list")

    return render(request, "products/productline_confirm_delete.html", {"productline": pl})
