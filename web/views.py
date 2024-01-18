from django.shortcuts import render
from . models import Emails
from . models import Contact,Quote





# Create your views here.

def index(request):
     
    if request.method=='POST':
        if request.POST.get("form_lists"):
            email=request.POST.get("emailstart")

            form_9 = Emails(

                Email = email)

            form_9.save()
     
        elif request.POST.get("form_list"):

                name=request.POST.get("name_2")
                email=request.POST.get("email_2")
                phone=request.POST.get("phone_2")
                service=request.POST.get("service_2")
                message=request.POST.get("messages_2")


                from_7 = Contact(

                    Name = name,
                    Email = email,
                    Phone = phone,
                    Service = service,
                    Message = message

                )
                from_7.save()

    query = request.GET.get('query')
    results = []

    if query:
        results = Search.objects.filter(title__icontains=query)
    print(results)
            
    return render(request,'web/index.html')

    







def index2(request):

    if request.method=='POST':
        if request.POST.get("form_lists"):
            email=request.POST.get("emailstart")

            form_9 = Emails(

                Email = email)

            form_9.save()
     
        elif request.POST.get("form_list"):

                name=request.POST.get("name_2")
                email=request.POST.get("email_2")
                phone=request.POST.get("phone_2")
                service=request.POST.get("service_2")
                message=request.POST.get("messages_2")


                from_7 = Contact(

                    Name = name,
                    Email = email,
                    Phone = phone,
                    Service = service,
                    Message = message

                )
                from_7.save()

            
    return render(request,'web/folder/index-2.html')

    






def service(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    return render(request,'web/folder/service.html')






def aboutus(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()
    return render(request,'web/folder/about-us.html')






def aboutusextend(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    return render(request,'web/folder/about-us-extend.html')







def blogsingle(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()
            
    return render(request,'web/folder/blog-single.html')













from .models import Search,Search2,Tag
from django.core.paginator import Paginator
def blog(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()


    query = request.GET.get('query')
    tag_filter = request.GET.get('tag')
    qs = Search.objects.all()
    hi = Search2.objects.all()
    # cate = Tag.objects.all()

    tags = Tag.objects.all()
    
    if query:
        qs = Search.objects.filter(title__icontains=query) | Search.objects.filter(content__icontains=query) 
        hi = Search2.objects.filter(title__icontains=query)

    if tag_filter:
        qs = qs.filter(cate__name=tag_filter)

       
    paginator = Paginator(qs, 2)
    page_number = request.GET.get('page')
    qsfinal = paginator.get_page(page_number)
    totolpage=qsfinal.paginator.num_pages

    # date = {
    #     'post': qs,
    #     'posts': hi,
    #     'tags': tags,
    #     'lastpage':totolpage,
    #     'totalpagelist': [n+1 for n in range(totolpage)]
        
    # }
       
    date = {
    'post': qs,
    'posts': hi,
    'tags': tags,
    'lastpage':totolpage,
    'totalpagelist': [n+1 for n in range(totolpage)],
    'current_page': page_number,  # Add this line
    }

    return render(request,'web/folder/blog.html',date)



# from django.core.paginator import Paginator
# from django.shortcuts import render
# from .models import Search, Search2, Tag

# def blog(request):
#     query = request.GET.get('query')
#     tag_filter = request.GET.get('tag')

#     qs = Search.objects.all()
#     hi = Search2.objects.all()
#     tags = Tag.objects.all()

#     if query:
#         qs = qs.filter(title__icontains=query) | qs.filter(content__icontains=query)
#         hi = hi.filter(title__icontains=query)

#     if tag_filter:
#         qs = qs.filter(cate__name=tag_filter)

#     paginator = Paginator(qs, 7)  # Change the number to adjust items per page
#     page_number = request.GET.get('page')
#     qsfinal = paginator.get_page(page_number)
#     total_pages = paginator.num_pages

#     context = {
#         'post': qsfinal,
#         'posts': hi,
#         'tags': tags,
#         'total_pages': total_pages,
#         'current_page': page_number,
#     }

#     return render(request, 'web/folder/blog.html', context)















def error404(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/error-404.html')











def faqsextend(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()


    return render(request,'web/folder/faqs-extend.html')






def galleryextend(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

  
    return render(request,'web/folder/gallery-extend.html')







def galleryphotosall(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()


    return render(request,'web/folder/gallery-photos-all.html')






def galleryphotos(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    return render(request,'web/folder/gallery-photos.html')






def gallery(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

  
    return render(request,'web/folder/gallery.html')





def getaquote(request):
      
    if request.method=="POST":
            if request.POST.get("form_list") == 'form6':
                name=request.POST.get("quote-request-name")
                email=request.POST.get("quote-request-email")
                phone=request.POST.get("quote-request-phone")
                company=request.POST.get("quote-request-company")
                Services=request.POST.get("quote-request-interest[]")
                Best=request.POST.get("quote-request-reach")
                Hear=request.POST.get("quote-request-hear")
                messages=request.POST.get("quote-request-message")

                form_9 = Quote(
                    name=name,
                    email=email,
                    phone=phone,
                    company=company,
                    Services=Services,
                    Best=Best,
                    Hear=Hear,
                    messages=messages
                )
                
                form_9.save()

            elif request.POST.get("form_lists"):
                
                Email=request.POST.get("emailstart")

                from_7 = Emails(

                    Email=Email
                )

                from_7.save()

            
    return render(request,'web/folder/get-a-quote.html')

    







def faqs(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/faqs.html')






def megamenu(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

  
    return render(request,'web/folder/megamenu.html')





from django.shortcuts import render
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        if request.POST.get("form_lists"):
            email = request.POST.get("emailstart")
            form_9 = Emails(Email=email)
            form_9.save()

        elif request.POST.get("form_list"):
            name = request.POST.get("name_2")
            email = request.POST.get("email_2")
            phone = request.POST.get("phone_2")
            service = request.POST.get("service_2")
            message = request.POST.get("messages_2")

            from_7 = Contact(
                Name=name,
                Email=email,
                Phone=phone,
                Service=service,
                Message=message
            )
            from_7.save()

            # Redirect to WhatsApp
            phone_number = '919562157043'
            text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nMessage: {message}"
            whatsapp_url = f"https://wa.me/{phone_number}?text={text}"
            return HttpResponseRedirect(whatsapp_url)

    return render(request,'web/folder/contact.html')








def productsingle(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    
    return render(request,'web/folder/product-single.html')






def projectsingle(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    return render(request,'web/folder/project-single.html')






def projectsextend(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/projects-extend.html')






def projects(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    
    return render(request,'web/folder/projects.html')







def products(request):
    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/products.html')







def serviceextend(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/service-extend.html')






def servicesingle2(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    
    return render(request,'web/folder/service-single-2.html')






def servicesingle(request):
        if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()
    
        return render(request,'web/folder/service-single.html')





def teams(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

    
    return render(request,'web/folder/teams.html')


def teamsingle(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/team-single.html')






def typography(request):

    if request.method=="POST":
            Email=request.POST.get("EMAIL")

            from_7 = Emails(

                Email=Email
            )

            from_7.save()

   
    return render(request,'web/folder/typography.html')














