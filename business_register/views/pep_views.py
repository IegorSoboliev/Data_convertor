from csv import reader


from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from business_register.filters import PepFilterSet
from business_register.models.pep_models import Pep
from business_register.permissions import PepSchemaToken
from business_register.serializers.company_and_pep_serializers import PepListSerializer, PepDetailSerializer
from data_converter.filter import DODjangoFilterBackend
from data_ocean.views import CachedViewSetMixin, RegisterViewMixin


@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['pep']))
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['pep']))
@method_decorator(name='retrieve_by_source_id', decorator=swagger_auto_schema(auto_schema=None))
class PepViewSet(RegisterViewMixin,
                 CachedViewSetMixin,
                 viewsets.ReadOnlyModelViewSet):
    permission_classes = [RegisterViewMixin.permission_classes[0] | PepSchemaToken]
    queryset = Pep.objects.all()
    serializer_class = PepListSerializer
    filter_backends = (DODjangoFilterBackend, SearchFilter)
    filterset_class = PepFilterSet
    search_fields = (
        'fullname', 'fullname_transcriptions_eng', 'pep_type',
        'last_job_title', 'last_employer',
    )
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PepDetailSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=True, url_path='/source-id', serializer_class=PepDetailSerializer)
    @method_decorator(cache_page(settings.CACHE_MIDDLEWARE_SECONDS))
    def retrieve_by_source_id(self, request, pk):
        pep = get_object_or_404(self.get_queryset(), source_id=pk)
        serializer = self.get_serializer(pep)
        return Response(serializer.data)

    @action(methods=['get', 'post'], detail=False, url_name='check-persons', serializer_class=PepListSerializer)
    def check_persons(self, request):
        # ToDo: define how we getting file from the front-end
        #  (if uploading: file = request.FILES['file'] we can use another reader here)
        file = 'path'
        results = Pep.objects.none()
        with open(file, newline='') as csvfile:
            for row in reader(csvfile):
                value = ''.join(row).lower()
                if value:
                    result = Pep.objects.filter(fullname__search=value)
                    results = results | result
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
