from django.contrib import admin
from information.models import Information, Developer, Award


class AwardsInline(admin.TabularInline):
    model = Information.awards.through


class DevelopmentInline(admin.TabularInline):
    model = Information.developers.through


class InformationAdmin(admin.ModelAdmin):
    inlines = [AwardsInline, DevelopmentInline, ]
    exclude = ('developers', 'awards', )


class AwardAdmin(admin.ModelAdmin):
    inlines = [AwardsInline, DevelopmentInline, ]


class DeveloperAdmin(admin.ModelAdmin):
    inlines = [AwardsInline, DevelopmentInline, ]


admin.site.register(Developer)
admin.site.register(Award)
