from django.contrib import admin
from django.utils.html import format_html
from .models import About

class AdminAbout(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'photo_preview', 'email', 'years_of_experience', 'location')
    search_fields = ('full_name', 'title', 'email', 'location', 'specialties')
    list_filter = ('years_of_experience', 'location', 'services')
    ordering = ('full_name',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'title', 'photo', 'short_bio', 'location')
        }),
        ('Professional Summary', {
            'fields': ('bio', 'years_of_experience', 'specialties')
        }),
        ('Education & Experience', {
            'fields': ('education', 'work_experience')
        }),
        ('Skills & Technologies', {
            'fields': ('programming_languages', 'frameworks', 'tools')
        }),
        ('Services', {
            'fields': ('services',)
        }),
        ('Contact & Social Links', {
            'fields': ('email', 'phone_number', 'linkedin', 'github', 'twitter')
        }),
        ('Achievements & Projects', {
            'fields': ('certifications', 'projects')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.photo.url)
        return "No Image"

    photo_preview.short_description = "Profile Photo"

# Register the model
admin.site.register(About, AdminAbout)
