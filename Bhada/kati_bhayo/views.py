from django.shortcuts import render, HttpResponse
from kati_bhayo.forms import katibhayoForm

#landing views page for the calculation
def dashboard(request):
    #showing form if the method is get
    form = katibhayoForm()
    if request.method == 'GET':
        return render(request, 'main_form.html', {'form':form})
    #else getting data calculating and returing to the bill.html after calculation as the method is post
    else:

        rate = 14
        initial_fare = 25
        data = request.POST
        for key, val in data.items():
            if key == 'distance':
                dist = eval(val)
            elif key == 'time_stamp':
                time_stamp = val
        time_stamp = time_stamp.split(":")
        try:

            hour = int(time_stamp[0])
            minute = int(time_stamp[1])
            #applying condition to the time so out of bound vairables are checked
            if hour in range(0, 24) and minute in range(0, 60):
                #applying the given conditions for the rates according to the time
                if hour in range(7,21):
                    initial_fare = initial_fare+ dist * rate
                    g_tot = initial_fare
                    return render(request, 'bill.html', {'distance': dist, 'surge': '0%', 'service_charge': '0%',
                                                         'rate':rate, 'initial':initial_fare, 'g_tot':g_tot})
                elif hour in range(5,7):
                    initial_fare = initial_fare + dist * rate
                    g_tot = initial_fare + initial_fare* 0.1
                    return render(request, 'bill.html', {'distance': dist, 'surge': '10%', 'service_charge': '0%',
                                                         'rate': rate,'initial':initial_fare, 'g_tot':g_tot})
                elif hour in range(0,5):
                    initial_fare = initial_fare + dist*rate
                    g_tot =initial_fare + initial_fare*0.5 +initial_fare*0.05
                    return render(request, 'bill.html', {'distance': dist, 'surge': '50%', 'service_charge': '5%',
                                                         'rate': rate, 'initial': initial_fare, 'g_tot': g_tot})
                elif hour in range(21, 23):
                    initial_fare = initial_fare + dist*rate
                    g_tot = initial_fare + initial_fare*0.15
                    return render(request, 'bill.html', {'distance': dist, 'surge': '15%', 'service_charge': '0%',
                                                         'rate': rate, 'initial': initial_fare, 'g_tot': g_tot})
                else:
                    initial_fare = initial_fare + dist*rate
                    g_tot = initial_fare + initial_fare*0.2
                    return render(request, 'bill.html', {'distance': dist, 'surge': '20%', 'service_charge': '0%',
                                                         'rate': rate, 'initial': initial_fare, 'g_tot': g_tot})
            else:
                return HttpResponse("time stamp is from 00:00 to 23:59")

        except IndexError:
            print("please stick to the format")

