from django.shortcuts import render
from pathlib import Path
from django.contrib.admin.views.decorators import staff_member_required

BASE_DIR = Path(__file__).resolve().parent.parent.parent


@staff_member_required
def list_slides(request):
    return render(request, "demo/slides.html")


@staff_member_required
def list_layouts(request):
    return render(request, "demo/layouts.html")


@staff_member_required
def styleTable(table):
    table = '<div class="markdownlog">' + table + '</div>'
    table = table.replace('<h2>', '<h2 class="py-8 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl">') \
    .replace('<td>', '<td class="px-2 py-2">') \
    .replace('<a ', '<a class="inline-flex items-center px-3 py-2 text-sm underline font-medium" target="_blank"')
    # .replace('<a ', '<a class="inline-flex items-center px-3 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 min-w-full" target="_blank"')
    return table