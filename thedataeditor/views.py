import os
from pathlib import Path
from urllib import request as urllib_request

from django.http import HttpResponse, Http404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NodeCategory, Node, Workflow, NodeItem, Connection
from .serializers import (
    NodeCategorySerializer,
    NodeSerializer,
    WorkflowSerializer,
    NodeItemSerializer,
    ConnectionSerializer
)

#from .mixins import *


class NodeCategoryListCreate(generics.ListCreateAPIView):
    queryset = NodeCategory.objects.all()
    serializer_class = NodeCategorySerializer


class NodeCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NodeCategory.objects.all()
    serializer_class = NodeCategorySerializer


class NodeListCreate(generics.ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class WorkflowListCreate(generics.ListCreateAPIView):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class WorkflowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class WorkflowBulkDelete(generics.GenericAPIView):
    queryset = Workflow.objects.all()

    def post(self, request):
        ids = request.data
        for workflow_id in ids:
            workflow = Workflow.objects.get(id=workflow_id)
            workflow.delete()
        return Workflow(ids, status=status.HTTP_200_OK)


class NodeItemListCreate(generics.ListCreateAPIView):
    queryset = NodeItem.objects.all()
    serializer_class = NodeItemSerializer


class NodeItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NodeItem.objects.all()
    serializer_class = NodeItemSerializer

"""
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request_data_eval = eval(request.data['out_data']['original_id'])
        request_data = request_data_eval(request.data)
        serializer = self.get_serializer(instance, data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
"""

class NodeItemUpdate(generics.UpdateAPIView):
    queryset = NodeItem.objects.all()
    serializer_class = NodeItemSerializer


class ConnectionListCreate(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class ConnectionNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class DownloadFile(APIView):

    def post(self, request):
        base_dir = Path(__file__).resolve().parent
        node_item = request.data
        filename = node_item['filename']
        filepath = os.path.join(base_dir, "mixins", "files", filename)
        p = Path(filepath)
        urllib_request.urlretrieve(p.as_uri(), filename)
        return Response(status=status.HTTP_204_NO_CONTENT)
