from django.http import HttpResponse
from django.contrib import admin

from . models import Outward, OutwardPic


def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=outward_correspondence.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u'id'),
        smart_str(u'date_received'),
        smart_str(u'date_despatched'),
        smart_str(u'subject'),
        smart_str(u'ref_no'),
        smart_str(u'address'),
        smart_str(u'despatch_mode'),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.date_received),
            smart_str(obj.date_despatched),
            smart_str(obj.subject),
            smart_str(obj.ref_no),
            smart_str(obj.address),
            smart_str(obj.despatch_mode),
        ])
    return response


export_csv.short_description = u'Eport CSV'


class OutwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_received', 'date_despatched',
                    'subject', 'ref_no', 'address', 'despatch_mode',)
    list_filter = ('date_received', 'date_despatched', 'ref_no',)
    search_fields = ('address', 'ref_no',)
    actions = [export_csv]


admin.site.register(Outward, OutwardAdmin)


class OutwardPicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imagefile', 'created_on',)
    list_filter = ('name', 'created_on',)
    search_fields = ('name',)


admin.site.register(OutwardPic, OutwardPicAdmin)
