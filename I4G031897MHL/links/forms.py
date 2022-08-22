from dataclasses import fields
from django import forms
from .models import Link

class TodoAppForm(forms):
    class Meta:
        model = Link
        fields = [
            "target_url",
            "description",
            "identifier",
            "author",
            "created_date",
            "active"
        ]