from django.shortcuts import render, redirect
from django.views.generic import ListView

from datetime import timedelta
from django.utils import timezone

from .models import Message, MessageImage
from .forms import MessageForm, MessageImageForm


class MessageViews(ListView):
    """ Generic view to show the list of messages"""

    model = Message
    template_name = "text_messenger/home.html"
    context_object_name = "messages"
    paginate_by = 10

    def get_ordering(self):
        """ Set the ordering to the list """
        ordering = self.request.GET.get("ordering", "date_published")
        return ordering

    def get_queryset(self):
        """ Check full or partly set to return """
        if self.request.GET.get("query") == "last24":
            time_threshold = timezone.now() - timedelta(hours=24)
            return Message.objects.filter(date_published__gt=time_threshold)
        return super().get_queryset()


class UserMessageViews(ListView):
    """ Generic view to show the list of users messages"""

    model = Message
    template_name = "text_messenger/home.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.filter(author=self.kwargs["pk"])


def new_message(request):
    """ View for creating new messages """
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        message_image_form = MessageImageForm(request.POST, request.FILES)

        # Check if message form fields is valid
        if message_form.is_valid():
            content = message_form.cleaned_data["content"]

            message = Message.objects.create(
                content=content,
                author=(request.user if request.user.is_authenticated else None),
            )

            # if image exists and form fields is valid => create new entry
            if message_image_form.files.get("images") and message_image_form.is_valid():
                images = message_image_form.files.getlist("images")
                for image in images:
                    obj = MessageImage.objects.create(image=image, message=message)
                    obj.save()

            # redirect to home page
            return redirect("home")

    context = {
        # check if user is authenticated and set initial value to field
        # 'message_form': MessageForm(initial={'author': request.user if request.user.is_authenticated else None}),
        "message_form": MessageForm(),
        "message_image_form": MessageImageForm(),
    }

    return render(request, "text_messenger/new_message.html", context=context)


def about(request):
    """ View for about page """
    return render(request, "text_messenger/about.html")
