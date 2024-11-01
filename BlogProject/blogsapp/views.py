from blogsapp.models import Blog
from blogsapp.serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# ดึงข้อมูลบทความทั้งหมด (GET) / บันทึกข้อมูลบทความใหม่ (POST)
class BlogList(APIView):
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ดึงข้อมูลบทความที่สนใจ (GET) / อัพเดทบทความ (PUT) / ลบบทความ (DELETE)
class BlogDetail(APIView):
    pass

'''

Function based viws
@api_view(['GET','PUT','DELETE'])
def blog_detail(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # แก้ไขเป็น serializer.errors
'''