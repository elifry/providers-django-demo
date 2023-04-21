from django.contrib import admin

from .models import BuildData

class BuildDataAdmin(admin.ModelAdmin):
    list_display = ("project_slug", "version", "branch", "status", "note", "started", "duration")
    list_filter = ("project_slug", "branch", )
    search_fields = ["project_slug", "version",]
    # prepopulated_fields = {"project_slug": ("name",)}

admin.site.register(BuildData, BuildDataAdmin)


from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "version", "branch", "status", "note", "started", "duration")
    list_filter = ("name", "branch", )
    search_fields = ["name", "version",]
    prepopulated_fields = {"project_slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
