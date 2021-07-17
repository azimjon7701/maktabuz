from rest_framework import routers
from parents.views import ParentView
from region.views import RegionView
from staff.views import StaffView
from school.views import *
router = routers.DefaultRouter()
router.register(r'parent',ParentView,basename='parent')
router.register(r'region',RegionView,basename='region')
router.register(r'staff',StaffView,basename='staff')
router.register(r'school',SchoolView,basename='school')
router.register(r'class',ClassView,basename='class')
router.register(r'pupil',PupilView,basename='pupil')
router.register(r'new',NewView,basename='new')
router.register(r'event',EventView,basename='event')
router.register(r'course',CourseView,basename='course')
router.register(r'subject',SubjectView,basename='subject')