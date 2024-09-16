from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from online_course.models import Course, Teacher, Category, Blog, Video, Comment


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'get_teachers', 'preview_image')
    search_fields = ('name', 'category__title')
    list_filter = ('category',)

    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')
        return 'No image'

    preview_image.short_description = 'Image'

    def get_teachers(self, obj):
        return ", ".join(
            [teacher.full_name for teacher in obj.teachers.all()]) if obj.teachers.exists() else 'No teachers'

    get_teachers.short_description = 'Teachers'


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('id', 'full_name', 'preview_image')

    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')
        return 'No image'

    preview_image.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'preview_image')

    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')
        return 'No image'

    preview_image.short_description = 'Image'


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('title', 'body', 'category', 'image', 'description')
    search_fields = ('title', 'category__title')
    list_filter = ('category',)


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    list_display = ('title', 'course', 'file')
    search_fields = ('title', 'course__name')
    list_filter = ('course',)


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('user', 'text', 'created_at')
    search_fields = ('user__username', 'text')
    list_filter = ('created_at', 'video')
    ordering = ('-created_at',)
