from .models import Category, Regions

def subject_renderer(request):
    data = {
        'all_category':  Category.objects.all()
    }
    return data


def regions_processor(request):
    data = {
        'all_regions':  Regions.objects.all()
    }
    return data




