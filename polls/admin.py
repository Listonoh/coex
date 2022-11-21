from django.contrib import admin

from polls.models import RandomGenerator


# Register your models here.
@admin.register(RandomGenerator)
class RandomGeneratorAdmin(admin.ModelAdmin):
    list_display = ('from_number', 'to_number', 'timestamp')
    list_filter = ('from_number', 'to_number', 'timestamp')
    search_fields = ('from_number', 'to_number', 'timestamp')
    readonly_fields = ('timestamp', 'result_list')