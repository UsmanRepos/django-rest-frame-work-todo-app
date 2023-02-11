from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import TodoSerializer, LoginSerializer
from .models import Todo, Time


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            token =  serializer.data.get('token')
            return Response(data={"status":"200","message":"success", "token": token}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class TodoViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset.filter(user = request.user.id)
        if search:
            queryset = queryset.filter(first_name__startswith = search)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        data = request.data
        todo = Todo.objects.create(
            todo_title=data['todo_title'],
            todo_description=data['todo_description'],
            is_done=data['is_done']
        )
        todo.save()

        time = Time.objects.get(pk=data.get('time'))
        todo.time = time
        todo.user = request.user

        student_serializer = self.get_serializer(todo)
        return Response(student_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs): 
        data = request.data
        time = data.pop('time')
        user = data.pop('user')
        todo = self.get_object()

        todo.todo_title = data.get('todo_title', todo.todo_title)
        todo.todo_description = data.get('todo_description', todo.todo_description)
        todo.is_done = data.get('is_done', todo.is_done)
        todo.time = Time.objects.get(pk=time)
        todo.user = User.objects.get(pk=user)
        todo.save()

        serializer = self.get_serializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
