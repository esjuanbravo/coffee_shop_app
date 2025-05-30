from django import forms
from .models import Products
from django.core.validators import FileExtensionValidator


class ProductsForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_field_styles()
        self.add_currency_to_price()
        self.customize_checkbox()

    def set_field_styles(self):
        base_styles = "w-full px-4 py-2.5 border rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all"

        self.fields["name"].widget.attrs.update(
            {"class": f"{base_styles}", "placeholder": "Ej: Cappuccino Premium..."}
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": f"{base_styles} h-32 resize-none",
                "placeholder": "Descripción detallada...",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": f"{base_styles}", "min": "0.50", "step": "0.10"}
        )

        self.fields["category"].widget.attrs.update(
            {"class": f"{base_styles} cursor-pointer"}
        )

        self.fields["imagen"].widget.attrs.update(
            {"class": "hidden", "accept": "image/*"}
        )

    def add_currency_to_price(self):
        self.fields["price"].label = "Precio (USD)"
        self.fields["price"].widget.attrs["inputmode"] = "numeric"

    def customize_checkbox(self):
        self.fields["available"].label = "¿Producto disponible actualmente?"
        self.fields["available"].widget.attrs.update(
            {
                "class": "w-5 h-5 text-emerald-600 border-2 border-gray-300 rounded-lg focus:ring-emerald-500 cursor-pointer"
            }
        )

    class Meta:
        model = Products
        fields = ["name", "description", "price", "imagen", "category", "available"]
        widgets = {
            "imagen": forms.FileInput(
                attrs={"class": "absolute w-full h-full opacity-0 cursor-pointer"}
            ),
        }
        labels = {
            "name": "Nombre del Producto",
            "description": "Descripción Detallada",
            "category": "Categoría del Producto",
        }
        help_texts = {
            "imagen": "Formatos soportados: JPG, PNG, WEBP (Máx. 5MB)",
            "category": "Selecciona la categoría más adecuada para el producto a resgistrar.",
        }
        error_messages = {
            "name": {
                "required": "Este campo es obligatorio",
                "max_length": "El nombre es demasiado largo (máx. 150 caracteres)",
            },
            "price": {
                "required": "Debes especificar un precio",
                "invalid": "Ingresa un valor numérico válido",
            },
        }

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")
        if imagen:
            # Validación de tamaño (exclusiva del formulario)
            if imagen.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError(
                    "La imagen es demasiado grande (máximo 5MB)"
                )

        return imagen

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            name = name.title()

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            description = description.title()
            description = description.strip()
            if not description.endswith("."):
                description += "."

        return description
