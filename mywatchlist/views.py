from django.shortcuts import render
from mywatchlist.models import AttributeWatchList

# Create your views here.
def watch_counter(query):
    msg = ""
    done_count = 0
    ongoing_count = 0
    queued_count = 0

    for atr in query:
        if atr.watched == "completed":
            done_count += 1
        elif atr.watched == "ongoing":
            ongoing_count += 1
        else:
            queued_count += 1

    return done_count

def show_watchlist(request):
    data_watchlist = AttributeWatchList.objects.all()
    message = watch_counter(data_watchlist)
    context = {
        'list_atr' : data_watchlist,
        'nama' : 'Arya Daniswara Khairan',
        'id' : '2106702781',
        'message' : message
    }
    return render(request, "watchlist.html", context)