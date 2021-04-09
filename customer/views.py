from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"customer/index.html")
def inner_page(request):
    return render(request,"customer/inner-page.html")
def portfolio_detail(request):
    return render(request,"customer/portfolio-details.html")

def portfolio(request):
    return render(request,"customer/portfolio.html")