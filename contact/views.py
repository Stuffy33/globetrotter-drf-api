from rest_framework import generics
from .models import Contact
from .serializer import ContactSerializer


class ContactDetail(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()