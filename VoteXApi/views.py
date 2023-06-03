from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from .models import User
from .rest_serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'home_page.html', {})


# example for creating api page

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# reference from labs1-4

# def import_view_all(request):
#     # df = pd.read_csv("uklonapp/all.csv", header=None, names=range(7))
#     with open("uklonapp/data.csv") as f:
#         reader = csv.reader(f)
#         count = -1
#         for row in reader:
#             print(row)
#             if row[0] == 'id':
#                 count += 1
#                 continue
#             if count == 0:
#                 _, created = User.objects.get_or_create(
#                     password=row[1],
#                     email=row[2],
#                     register_date=row[3],
#                 )
#             if count == 1:
#                 _, created = Pax.objects.get_or_create(
#                     user_id=row[1],
#                     name=row[2],
#                     phone_number=row[3],
#                     card_info=row[4],
#                 )
#             if count == 2:
#                 _, created = Driver.objects.get_or_create(
#                     user_id=row[1],
#                     name=row[2],
#                     car_name=row[3],
#                     rating=row[4],
#                     phone_number=row[5],
#                     card_info=row[6],
#                 )
#             if count == 3:
#                 _, created = Ride.objects.get_or_create(
#                     pax_id=row[1],
#                     driver_id=row[2],
#                     start_gps=row[3],
#                     end_gps=row[4],
#                     payment_method=row[5],
#                     stars=row[6],
#                 )
#     response = HttpResponse('Import Successful!')
#     return response
#
#
# def create_ride(request):
#     form = RideForm()
#     if request.method == 'POST':
#         form = RideForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/export_ride')
#
#     context = {'form': form}
#     return render(request, 'create_ride.html', context)
#
#
# def update_ride(request, pk):
#     ride = Ride.objects.get(id=pk)
#     form = RideForm(instance=ride)
#     if request.method == 'POST':
#         form = RideForm(request.POST, instance=ride)
#         if form.is_valid():
#             form.save()
#             return redirect('/export_ride')
#     context = {'form': form}
#     return render(request, 'create_ride.html', context)
#
#
# def delete_ride(request, pk):
#     ride = Ride.objects.get(id=pk)
#     if request.method == "POST":
#         ride.delete()
#         return redirect('/export_ride')
#     context = {'item': ride}
#     return render(request, 'delete_ride.html', context)
#
#
# class RideListView(ListView, FormView):
#     queryset = Ride.objects.all()
#     template_name = 'export_ride.html'
#     form_class = FormatForm
#
#     def post(self, request, **kwargs):
#         qs = self.queryset
#         dataset = RideResource().export(qs)
#         data_format = request.POST.get('format')
#         if data_format == 'xls':
#             ds = dataset.xls
#         elif data_format == 'csv':
#             ds = dataset.csv
#         else:
#             ds = dataset.json
#
#         response = HttpResponse(ds, content_type=f"{data_format}")
#         response['Content-Disposition'] = f"attachment; filename=Ride.{data_format}"
#         return response
#
#
# class AllListView(ListView, FormView):
#     model = User
#     template_name = 'all.html'
#     context_object_name = 'all'
#     form_class = FormatForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(user=User.objects.all(), pax=Pax.objects.all(), driver=Driver.objects.all(),
#                        ride=Ride.objects.all())
#         return context
#
#     def post(self, request, **kwargs):
#         dataset1 = UserResource().export(User.objects.all())
#         dataset2 = PaxResource().export(Pax.objects.all())
#         dataset3 = DriverResource().export(Driver.objects.all())
#         dataset4 = RideResource().export(Ride.objects.all())
#         data_format = request.POST.get('format')
#         if data_format == 'xls':
#             ds = dataset1.xls + \
#                  dataset2.xls + \
#                  dataset3.xls + \
#                  dataset4.xls
#         elif data_format == 'csv':
#             ds = dataset1.csv + \
#                  dataset2.csv + \
#                  dataset3.csv + \
#                  dataset4.csv
#         else:
#             ds = dataset1.json + \
#                  dataset2.json + \
#                  dataset3.json + \
#                  dataset4.json
#
#         response = HttpResponse(ds, content_type=f"{data_format}")
#         response['Content-Disposition'] = f"attachment; filename=all.{data_format}"
#         return response
