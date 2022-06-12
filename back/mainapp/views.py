import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

class TaskView(View):
    def get(self, request):    
        # json形式でレスポンスを返す
        return JsonResponse("tasks_list", safe=False, status=200)