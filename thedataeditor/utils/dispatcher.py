from .read_csv import read_csv
from .read_json import read_json

READER_FUNCTIONS = {
    "read_csv": read_csv,
    "read_json": read_json,
}
def get_reader_function(original_id):
    return READER_FUNCTIONS.get(original_id)


"""
from .utils.dispatcher import get_reader_function

class NodeItemUpdateFormData(generics.RetrieveUpdateAPIView):
    queryset = NodeItem.objects.all()
    serializer_class = NodeItemSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        request_data = request.data.copy()

        form_data = request_data.get('formData', {})
        file_id = form_data.get('file_id')
        node_item_id = form_data.get('node_item_id')

        original_id = instance.original_id

        # Get the corresponding function dynamically
        reader_function = get_reader_function(original_id)
        response_data = {}

        if reader_function:
            response_data = reader_function(file_id, node_item_id)

        request_data["response_data"] = response_data
        instance.response_data = response_data
        instance.save()

        serializer = self.get_serializer(instance, data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

"""