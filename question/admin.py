from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from .models import Narayana_Question,Chaithanya_Question,Narayana_Submission,Chaithanya_Submission
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import AdminSite
from import_export.admin import ImportExportActionModelAdmin

class NarayanaAdmin(ImportExportActionModelAdmin):
    pass

class NarayanaSubmissionAdmin(ImportExportActionModelAdmin):
    pass

class ChaithanyaSubmissionAdmin(ImportExportActionModelAdmin):
    pass

class ChaithanyaAdmin(ImportExportActionModelAdmin):
    pass

class NarayanaResource(resources.ModelResource):

    class Meta:
        model = Narayana_Question
        skip_unchanged = True
        report_skipped = False
        fields = ('id','question', 'option1','option2','option3','option4','correct_option')
        export_order = ('id','question', 'option1','option2','option3','option4','correct_option')

class NarayanaSubmissionResource(resources.ModelResource):

    class Meta:
        model = Narayana_Submission
        skip_unchanged = True
        report_skipped = False
        fields = ('id','name', 'data','score','time')
        export_order = ('id','name', 'data','score','time')

class ChaithanyaResource(resources.ModelResource):

    class Meta:
        model = Chaithanya_Question
        skip_unchanged = True
        report_skipped = False
        fields = ('id','question', 'option1','option2','option3','option4','correct_option')
        export_order = ('id','question', 'option1','option2','option3','option4','correct_option')

class ChaithanyaSubmissionResource(resources.ModelResource):

    class Meta:
        model = Chaithanya_Submission
        skip_unchanged = True
        report_skipped = False
        fields = ('id','name', 'data','score','time')
        export_order = ('id','name', 'data','score','time')

class NarayanaAdmin(ImportExportModelAdmin):
    resource_class = NarayanaResource

class ChaithanyaAdmin(ImportExportModelAdmin):
    resource_class = ChaithanyaResource

class NarayanaSubmissionAdmin(ImportExportModelAdmin):
    resource_class = NarayanaSubmissionResource
    fieldsets = [
    	(None, {'fields': ['name']}),
    	('JSON', {'fields': ['detail_nar_json_formatted']}),
    	(None, {'fields': ['score']}),
    	(None, {'fields': ['time']}),
        (None, {'fields': ['created']}),
    ]
    list_display = ('name','score','time')
    readonly_fields = ('data','detail_nar_json_formatted')


class ChaithanyaSubmissionAdmin(ImportExportModelAdmin):
    resource_class = ChaithanyaSubmissionResource
    fieldsets = [
    	(None, {'fields': ['name']}),
    	('JSON', {'fields': ['detail_chai_json_formatted']}),
    	(None, {'fields': ['score']}),
        (None, {'fields': ['time']}),
        (None, {'fields': ['created']}),
    ]
    list_display = ('name','score','time')
    readonly_fields = ('data','detail_chai_json_formatted')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.site_header = "SSS Admin"
admin.site.site_title = "SSS Admin Portal"
admin.site.index_title = "Welcome to SSS Portal"
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Narayana_Question,NarayanaAdmin)
admin.site.register(Chaithanya_Question, ChaithanyaAdmin)
admin.site.register(Narayana_Submission, NarayanaSubmissionAdmin)
admin.site.register(Chaithanya_Submission, ChaithanyaSubmissionAdmin)