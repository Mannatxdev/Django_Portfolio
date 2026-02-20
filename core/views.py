from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

# from django.shortcuts import render

# def coding_stats_view(request):
#     return render(request, "coding_stats.html")

from django.db.models import Sum
from .models import CodingStat

def coding_stats_view(request):
    stats = CodingStat.objects.all()
    total = stats.aggregate(Sum('problems_solved'))['problems_solved__sum'] or 0

    return render(request, "coding_stats.html", {
        "stats": stats,
        "total": total
    })