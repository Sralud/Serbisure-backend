from django.http import JsonResponse


def ServiceListView(request):
    """
    Placeholder view for listing services.
    Will be replaced with a full DRF view in Task 3.
    """
    return JsonResponse({
        "status": "success",
        "message": "Service list endpoint is working.",
        "data": []
    })
