from django.contrib import admin
from import_export.formats import base_formats
from import_export.admin import ImportExportModelAdmin
from user.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name')

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.JSON,
            base_formats.ODS

        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.JSON,
            base_formats.ODS

        )

        return [f for f in formats if f().can_export()]