from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User=get_user_model()

from .serializer import UserSerializer
print("COooming is the views")
from rest_framework.response import Response
from rest_framework import permissions, status


class RegisterView(APIView):
    print("IN RegisterView")
    permission_classes= (permissions.AllowAny,)

    def post(self, request):
        print("IN Post function")

        #try:
        data= request.data
        
        name= data['name']
        email= data['email']
        email= email.lower()
        password= data['password']
        pass2= data['re_password']
        is_realtor= data['is_realtor']

        print('name-', name,'email-', email, 'password--', password, 'pass2--', pass2, 'is_realtor--', is_realtor)

        if is_realtor=="True":
            is_realtor=True
        else:
            is_realtor= False
        
        if password==pass2:
            if len(password)>8:
                print("PAssed length parameters")
                if not User.objects.filter(email=email).exists():
                    if is_realtor==True:
                        User.objects.create_realtor(email=email, name= name, password=password)
                        
                        return Response({'success': 'Realtor account created successfuly'},
                                        status=status.HTTP_201_CREATED)
                    else:
                        User.objects.create_user(email=email, name= name, password=password)

                        return Response({'success': 'User created successfuly'},
                                        status=status.HTTP_201_CREATED)
                
                else:
                    return Response({'error':'This email is already in use'},
                                    status= status.HTTP_400_BAD_REQUEST)


            else:
                return Response({
                    'error':"Password must be greater than 8 words."},
                    status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Your Passwords don't match"},
                            status= status.HTTP_400_BAD_REQUEST)
        




        

class RetrieveView(APIView):
    def get(self, request):
        try:
            user= request.user
            user= UserSerializer(user)
            return Response({'user': user.data},
                            status= status.HTTP_200_OK)

        except:
            return Response({'error':'SOmething went wrong while retrieving user details'},
                            status= status.HTTP_500_INTERNAL_SERVER_ERROR)