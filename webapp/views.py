import multiprocessing
import datetime
import csv
import time

from django.utils.encoding import smart_str

from .models import Topic, Record
from django.shortcuts import render, HttpResponse, redirect

from .Detector import detect

process = multiprocessing.Process(target=detect)


def index(request, message=None):

    topic = Topic.objects.first()
    if topic is None:
        return render(request, 'webapp/home.html', {"message": 'No Topics Available !'})

    # Save Record
    add_record_with_start_time(topic.full_name)

    return render(request, 'webapp/home.html',
                  {"index": topic.id, "email": topic.full_name, "body": topic.roll_number, "message": message})


def insert(request):
    return render(request, 'webapp/insert.html')


def records(request):
    data = Record.objects.all().order_by('-start_time')
    return render(request, 'webapp/records.html', {"records": data})


def delete_topic(request):
    current_id = int(request.GET.get('index'))
    Topic.objects.filter(id=current_id).delete()

    return index(request,message='Message Deleted')


def next(request):
    # Add End Time of Previous Record
    update_last_record_with_end_time()

    # Fetch Next Record
    current_id = int(request.GET.get('index',0))
    topic=Topic.objects.filter(id__gt=current_id).order_by('id').first()
    if topic is None:
        return render(request, 'webapp/home.html', {"message": 'No More Records', "index": current_id + 1})

    # Add Record For Current Topic
    add_record_with_start_time(topic.full_name)

    return render(request, 'webapp/home.html', {"index": topic.id, "email": topic.full_name, "body": topic.roll_number})


def prev(request):
    # Add End Time of Previous Record
    update_last_record_with_end_time()

    current_id = int(request.GET.get('index',0))
    topic=Topic.objects.filter(id__lt=current_id).order_by('-id').first()
    if topic is None:
        return render(request, 'webapp/home.html', {"message": 'No More Records', "index": current_id - 1})

    # Add Record For Current Topic
    add_record_with_start_time(topic.full_name)

    return render(request, 'webapp/home.html', {"index": topic.id, "email": topic.full_name, "body": topic.roll_number})


def add(request):
    topic_name = request.GET.get('topic')
    topic_body = request.GET.get('topic_body')
    new_topic = Topic(full_name=topic_name, roll_number=topic_body)
    new_topic.save()

    return render(request, 'webapp/home.html',
                  {"index": new_topic.id, "email": new_topic.full_name, "body": new_topic.roll_number,
                   "message": "New Topic Added"})


def delete_records(request):
    record_id = int(request.GET.get('index'))
    Record.objects.filter(id=record_id).delete()
    return render(request, 'webapp/records.html', {"records": Record.objects.all()})


def clear_records(request):
    Record.objects.all().delete()
    return render(request, 'webapp/records.html', {"records": Record.objects.all()})


def download(request):
    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachment; filename="DataLog.csv"'
    writer = csv.writer(res, csv.excel)
    res.write(u'\ufeff'.encode('utf8'))
    writer.writerow(
        [smart_str(u"Topic Name"), smart_str(u"Start Time"), smart_str(u"End Time"), smart_str(u"Duration")])
    data_log = Record.objects.all()
    for log in data_log:
        writer.writerow(
            [smart_str(log.topic_name), smart_str(log.start_time), smart_str(log.end_time), smart_str(log.duration)])
    return res


def detect_on(request):
    process.start()
    return redirect(index)


def detect_off(request):
    process.terminate()
    process.exitcode
    return redirect(index)


def add_record_with_start_time(topic_name):
    record = Record(topic_name=topic_name, start_time = time.time())
    record.save()


def update_last_record_with_end_time():
    last_record = Record.objects.all().order_by("-id")
    if len(last_record)>0:
        last_record = last_record[0]
        if last_record.end_time is None:
            last_record.end_time = time.time()
            last_record.duration = last_record.end_time - float(last_record.start_time)
            last_record.start_time = time.ctime(float(last_record.start_time))
            last_record.end_time = time.ctime(last_record.end_time)
            last_record.save()


def sql_query_to_csv(query_output, columns_to_exclude=""):
    rows = query_output
    columns_to_exclude = set(columns_to_exclude)

    # create list of column names
    column_names = [i for i in rows[0].__dict__]
    for column_name in columns_to_exclude:
        column_names.pop(column_names.index(column_name))

    # add column titles to csv
    column_names.sort()
    csv = ", ".join(column_names) + "\n"

    # add rows of data to csv
    for row in rows:
        for column_name in column_names:
            if column_name not in columns_to_exclude:
                data = str(row.__dict__[column_name])
                # Escape (") symbol by preceeding with another (")
                data.replace('"', '""')
                # Enclose each datum in double quotes so commas within are not treated as separators
                csv += '"' + data + '"' + ","
        csv += "\n"

    return csv
