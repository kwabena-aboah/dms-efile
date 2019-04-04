from django.http import HttpResponse
from django.contrib import admin

from . models import Inward, InwardPic, DocumentUpload


def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=inward_correspondence.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u'id'),
        smart_str(u'date_of_letter'),
        smart_str(u'date_received'),
        smart_str(u'received_from'),
        smart_str(u'ref_no'),
        smart_str(u'subject'),
        smart_str(u'officer_to'),
        smart_str(u'date_filed'),
        smart_str(u'file_number'),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.date_of_letter),
            smart_str(obj.date_received),
            smart_str(obj.received_from),
            smart_str(obj.ref_no),
            smart_str(obj.subject),
            smart_str(obj.officer_to),
            smart_str(obj.date_filed),
            smart_str(obj.file_number),
        ])
    return response


export_csv.short_description = u'Eport CSV'


class InwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_letter', 'date_received',
                    'received_from', 'ref_no', 'subject', 'officer_to',
                    'date_filed', 'file_number',)
    list_filter = ('date_of_letter', 'date_received', 'date_filed',)
    search_fields = ('received_from', 'file_number',)
    actions = [export_csv]


admin.site.register(Inward, InwardAdmin)


class InwardPicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imagefile', 'created_on',)
    list_filter = ('name', 'created_on',)
    search_fields = ('name',)


admin.site.register(InwardPic, InwardPicAdmin)


class DocumentUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uploaded_on',)
    list_filter = ('name', 'uploaded_on',)

admin.site.register(DocumentUpload, DocumentUploadAdmin)