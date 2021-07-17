from rest_framework import viewsets
from .models import *
from .serializers import *
class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
class PupilView(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
class NewView(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer