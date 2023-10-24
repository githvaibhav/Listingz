from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listings
from rest_framework import status, permissions
from .serializer import ListingSerializer

# Create your views here.
class ManageListingView(APIView):
    def get(self, request, format=None):
        print('IN Func')
        try:
            print('IN try')
            user= request.user

            if not user.is_realtor:
                print('IN if')
                return Response({"error":"User don't have permission to view this listing"}, 
                                status= status.HTTP_403_FORBIDDEN)
            print('out if')
            slug= request.query_params.get('slug')
            if not slug:
                print('working fine')
                listings= Listings.objects.order_by('-date_created').filter(realtor= user.email)
                listings= ListingSerializer(listings, many=True)
                return Response({"listings":listings.data}, 
                                status=status.HTTP_200_OK)
            print('out slug')
            
            if Listings.objects.filter(
                realtor= user.email,
                slug=slug
            ).exists():
                listing = Listings.objects.get(realtor= user.email, slug=slug)
                listing = ListingSerializer(listing, many=False)
                return Response({"listings":listing.data}, 
                                status=status.HTTP_200_OK)

            else:
                return Response({"error":"Listing not found"}, 
                                status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"error":"Something went wrong while trying to retrieve this listing"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve_values(self, data):
        print("In funvtion")
        title= data['title']
        slug= data['slug']
        print("111111111111")
        
        print("22222222222222")
        address= data['address']
        city= data['city']
        state= data['state']
        zipcode= data['zipcode']
        description= data['description']
        price= data['price']
        print("Before try in func")
        try:
            price= int(price)
        except:
            return Response({"error":"Price must be an integer"},
                    status=status.HTTP_400_BAD_REQUEST)
        bedrooms= data['bedrooms']
        try:
            bedrooms= int(bedrooms)
        except:
            return Response({"error":"Bedrooms must be an integer"},
                    status=status.HTTP_400_BAD_REQUEST)
        bathrooms= data['bathrooms']
        try:
            bathrooms= float(bathrooms)
        except:
            return Response({"error":"Bathrooms must be a floating point number"},
                    status=status.HTTP_400_BAD_REQUEST)
        if bathrooms<=0 or bathrooms>10:
            bathrooms=1.0

        bathrooms= round(bathrooms,1)

        sale_type= data['sale_type']
        if sale_type=="FOR_SALE" or sale_type=="for_sale":
            sale_type= "For Sale"
        if sale_type=="FOR_RENT" or sale_type=="for_rent":
            sale_type= "For Rent"

        home_type= data['home_type']
        if home_type=="House" or home_type=="house":
            home_type= "House"
        if home_type=="Condo" or home_type=="condo":
            home_type= "Condo"
        if home_type=="TownHouse" or home_type=="townhouse":
            home_type= "TownHouse"

        main_photo= data['main_photo']
        photo1= data['photo1']
        photo2= data['photo2']
        photo3= data['photo3']

        is_published= data['is_published']
        if is_published=='True':
            is_published=True
            print("In publisjed if")
        else:
            is_published=False

        
        print("Will get the data ready now")
        data={

            "title": title,
            "slug": slug,
            "address": address,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "description": description,
            "price": price,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sale_type": sale_type,
            "home_type": home_type,
            "main_photo": main_photo,
            "photo1": photo1,
            "photo2": photo2,
            "photo3": photo3,
            "is_published": is_published
        }
        print("returning the data")
        return data
        

    def post(self, request):   
        try:
            user= request.user
            print("In try")
            if user.is_realtor:
                data= request.data
                print("In if")
                data= self.retrieve_values(data)
                print("After func")
                title = data['title']
                slug = data['slug']
                address = data['address']
                city = data['city']
                state = data['state']
                zipcode = data['zipcode']
                description = data['description']
                price = data['price']
                bedrooms = data['bedrooms']
                bathrooms = data['bathrooms']
                sale_type = data['sale_type']
                home_type = data['home_type']
                main_photo = data['main_photo']
                photo1 = data['photo1']
                photo2 = data['photo2']
                photo3 = data['photo3']
                is_published = data['is_published']
                print("After data retrieval")

                if Listings.objects.filter(slug=slug).exists():
                    return Response({"error":"Listing with this slig already exists"}, 
                                status= status.HTTP_400_BAD_REQUEST)
                
                Listings.objects.create(
                    realtor= user.email,
                    title=title,
                    slug=slug,
                    address=address,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    description=description,
                    price=price,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    sale_type=sale_type,
                    home_type=home_type,
                    main_photo=main_photo,
                    photo1=photo1,
                    photo2=photo2,
                    photo3=photo3,
                    is_published= is_published
                    )
                
                print("After creating a lising")
                return Response({"success":"Listing created successfully"}, 
                                status= status.HTTP_201_CREATED)


            else:
                return Response({"error":"User don't have permission to create this listing"}, 
                                status= status.HTTP_403_FORBIDDEN)

        except:
            return Response({"error":"Something went wrong while trying to Post"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            user= request.user
            if user.is_realtor:
                data=request.data
                print("In if")
                data= self.retrieve_values(data)
                print()
                title = data['title']
                slug = data['slug']
                address = data['address']
                city = data['city']
                state = data['state']
                zipcode = data['zipcode']
                description = data['description']
                price = data['price']
                bedrooms = data['bedrooms']
                bathrooms = data['bathrooms']
                sale_type = data['sale_type']
                home_type = data['home_type']
                main_photo = data['main_photo']
                photo1 = data['photo1']
                photo2 = data['photo2']
                photo3 = data['photo3']
                is_published = data['is_published']

                if not Listings.objects.filter(realtor= user.email, slug= slug).exists():
                    return Response({"error":"Listing doesn't exist"}, 
                                status= status.HTTP_404_NOT_FOUND)
                
                Listings.objects.filter(realtor=user.email, slug=slug).update(
                    realtor= user.email,
                    title=title,
                    slug=slug,
                    address=address,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    description=description,
                    price=price,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    sale_type=sale_type,
                    home_type=home_type,
                    main_photo=main_photo,
                    photo1=photo1,
                    photo2=photo2,
                    photo3=photo3,
                    is_published= is_published
                    )

                return Response({"success":"Listing updated successfully"}, 
                                status= status.HTTP_200_OK)
                

            else:
                return Response({"error":"User don't have permission to update this listing data"}, 
                                status= status.HTTP_403_FORBIDDEN)

        except:
            return Response({"error":"Something went wrong while trying to Post"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListingDetailView(APIView):
    def get(self,request, fotmat= None):
        try:
            print("In try")
            slug= request.query_params.get('slug')

            if not slug:
                return Response({'error': 'Slug nnot provided'},
                            status= status.HTTP_400_BAD_REQUEST)
            print("after taking slug")
            
            if not Listings.objects.filter(is_published=True, slug=slug).exists():
                return Response({'error': 'This entr does not exist'},
                            status= status.HTTP_404_NOT_FOUND)
            print("checked if this exists")
            
            listing= Listings.objects.get(is_published=True, slug=slug)
            print("getting the listing")
            listing= ListingSerializer(listing, many=False)
            
            print("serializied", listing.data)
            
            return Response({'listing': listing.data},
                            status= status.HTTP_200_OK)
                
                
        except:
            return Response({'error': 'Something went wrong while retrieving the Listings'},
                            status= status.HTTP_500_INTERNAL_SERVER_ERROR)




class ListingsView(APIView):
    permission_classes=(permissions.AllowAny,)
    def get(self, request):
        try:
            print("In try")
            if not Listings.objects.filter(is_published= True).exists():
                return Response({'error': 'No Published listings in the database'},
                        status= status.HTTP_404_NOT_FOUND)
            print("Yes there are listings")
            listinggs= Listings.objects.order_by('-date_created').filter(is_published= True)
            listinggs= ListingSerializer(listinggs, many=True)
            print("Got serialized")
            return Response({'listing': listinggs.data},
                            status= status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving Listings'},
                            status= status.HTTP_500_INTERNAL_SERVER_ERROR)
