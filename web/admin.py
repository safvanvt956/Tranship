from django.contrib import admin
from . models import Emails,Contact,Quote,Search,Search2,Tag


# Register your models here.


admin.site.register(Emails)





@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Service','Message')




@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display=('name','company','email','phone','Services','Best','Hear','messages')


    


@admin.register(Search)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","content","publish_timestamp",)
    search_fields = ("title","content","publish_timestamp",)
    list_filter = ("title","content","publish_timestamp",)






@admin.register(Search2)
class SecondAdmin(admin.ModelAdmin):
    list_display = ("title","image")
    search_fields = ("title","image")
    list_filter = ("title","image")




admin.site.register(Tag)


# admin.site.register(task)
# admin.site.register(red)




    

    



