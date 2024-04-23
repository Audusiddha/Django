from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project_api import serializers

# Import necessary modules and serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    # Define the serializer class to be used for request validation and serialization

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # Define a method to handle GET requests to the API endpoint

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        # Define a list of API view features

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        # Return a response containing a greeting message and the list of API view features
    
    
    def post(self, request):
        """Create a hello message with our name"""
        # Define a method to handle POST requests to the API endpoint

        serializer = self.serializer_class(data=request.data)
        # Create an instance of the serializer class with request data

        if serializer.is_valid():
            # Check if the data passed to the serializer is valid
            name = serializer.validated_data.get('name')
            # Extract the 'name' field from the validated data
            message = f'Hello {name}!'
            # Create a greeting message using the extracted name
            return Response({'message': message})
            # Return a response containing the greeting message
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            # If the data is not valid, return a response with serializer errors and HTTP status code 400


    def put(self, request, pk=None):
       """Handle updating an object"""
       # Define a method to handle PUT requests to the API endpoint
       return Response({'method': 'PUT'})
       # Return a response indicating that the method is PUT


    def patch(self, request, pk=None):
        """Handle partial update of object"""
        # Define a method to handle PATCH requests to the API endpoint

        return Response({'method': 'PATCH'})
        # Return a response indicating that the method is PATCH


    def delete(self, request, pk=None):
        """Delete an object"""
        # Define a method to handle DELETE requests to the API endpoint

        return Response({'method': 'DELETE'})
        # Return a response indicating that the method is DELETE
