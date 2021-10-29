import datetime
import json
import csv
from django import template
from django.shortcuts import render, HttpResponse, redirect

from textparse.models import Data
from textparse.models import Records
from .forms import InputText
from .parse import parse


# Create your views here.
def index(request):
    data = Data.objects.all()
    topics = [obj.topic for obj in data]
    body = [obj.body for obj in data]
    parsed = [obj.parsed for obj in data]
    keys_all = [obj.keys for obj in data]
    if request.method == "POST":
        topic = request.POST.get('subject')
        body = request.POST.get('content')
        recipient = request.POST.get('recipient')
        keys, final = parse(body)
        keys = json.dumps(keys)
        Data.objects.create(topic=topic, body=body, parsed=final, keys=keys, to=recipient)
        # data = Data.objects.all()
        # final = {"top": "Topic", "topic": topic, "bod": "Body", "final": final}
        # return render(request, 'textparse/index.html',
        #               {'topics': topics, 'body': body, 'parsed': parsed, 'b': body, 'oc': 'red', 'color': 'green',
        #                'keys': keys, 'final': final, 'objects': data})
        return redirect('text_parse_index')

    else:
        return render(request, 'textparse/index.html',
                      {
                          'keys': keys_all,
                          'topics': topics,
                          'body': body,
                          'parsed': parsed,
                          'oc': 'green', 'color': 'red',
                          'objects': data})


def detail(request):
    result = Data.objects.filter(id=request.GET.get('id'))  # all()
    all_records = Data.objects.all()
    for item in all_records:
        print(item.id)
    record_keys = [obj.id for obj in all_records]
    topics = [obj.topic for obj in result]
    parsed = [obj.parsed for obj in result]
    keys_all = [obj.keys for obj in result]
    body = [obj.body for obj in result]
    return render(request, 'textparse/detail.html',
                  {'detail': result[0],
                   'keys_all': keys_all,
                   'topics': topics,
                   'body': body,
                   'parsed': parsed,
                   'oc': 'green', 'color': 'red',
                   'id': request.GET.get('id'),
                   'record_keys': record_keys
                   })


def save_record(request):
    try:
        duration = datetime.timedelta(seconds=int(request.GET.get('time')))
        topic = request.GET['topic']
        now = datetime.datetime.now()
        end_time = now
        start_time = end_time - duration
        Records.objects.create(startTime=start_time, endTime=end_time,subject=topic, duration=duration.seconds)
        return HttpResponse(200)
    except KeyError:
        return HttpResponse('Invalid request', status=500)


def records_list(request):
    if request.method=="GET":
        data = Records.objects.all()
        return render(request, 'textparse/records.html', {'data': data})
    elif request.method == "POST":
        action = request.POST['action']
        if action == "delete":
            id = request.POST['id']
            record_id = Records.objects.get(id=id)
            record_id.delete()
            return redirect('text_parse_records')
        elif action == "delete_all":
            records = Records.objects.all()
            records.delete()
        return redirect('text_parse_records')

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    writer = csv.writer(response)
    writer.writerow(['Start Time', 'End Time', 'Created At', 'Duration'])

    users = Records.objects.all().values_list('startTime', 'endTime', 'createdAt','subject','duration')
    for user in users:
        test = user + ((user[1] - user[0]),)
        writer.writerow(test)

    return response


def delete_email(request):
    id = request.GET.get('id')
    Data.objects.filter(pk=id).delete()
    return HttpResponse(200)
