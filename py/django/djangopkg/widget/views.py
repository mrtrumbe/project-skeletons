from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required

@login_required
@render_to("widget/list.html")
def get_widgets(request):
    return {}

