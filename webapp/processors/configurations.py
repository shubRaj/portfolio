from ..models import Configuration


def defaults(request):
    response = {"has_config": Configuration.objects.exists()}
    if response.get("has_config"):
        config = Configuration.objects.first()
        response["full_name"] = config.full_name
        response["position"] = config.position
        response["profile"] = config.profile.url
        response["large_profile"] = config.large_profile.url
        response["about"] = config.about
        response["favicon"] = config.favicon.url
        response["description"] = config.description
    else:
        response["full_name"] = "Anonymous"
        response["position"] = "Undisclosed"
        response["profile"] = response["favicon"] = "https://img.icons8.com/bubbles/50/000000/user.png"
    return response
