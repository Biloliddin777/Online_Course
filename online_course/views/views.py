from django.views.generic import View, TemplateView, DetailView, ListView
from django.shortcuts import render
from online_course.models import Course, Category, Teacher, Blog, Video


class HomeView(View):
    template_name = 'online_course/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self):
        return {
            'categories': Category.objects.all(),
            'courses': Course.objects.all(),
            'teachers': Teacher.objects.all()
        }


class CategoryListView(View):
    template_name = 'online_course/base/base.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self):
        return {'categories': Category.objects.all()}


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'online_course/teacher.html'


class CourseListView(View):
    template_name = 'online_course/course.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self):
        return {
            'categories': Category.objects.all(),
            'courses': Course.objects.all()
        }


class CourseDetailView(DetailView):
    model = Video
    template_name = 'online_course/course_details.html'
    context_object_name = 'videos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(course=self.get_object().id)
        return context


class VideoDetailView(DetailView):
    model = Video
    template_name = 'online_course/video-detail.html'
    context_object_name = 'video'


class AboutView(TemplateView):
    template_name = 'online_course/about.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'online_course/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.all(),
            'teachers': Teacher.objects.all(),
            'videos': Video.objects.all(),
        })
        return context
