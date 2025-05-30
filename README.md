# Coffee Shop App

![Coffee Shop App Banner](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1050&q=80)

## Descripción

**Coffee Shop App** es un proyecto Django diseñado para gestionar un café moderno, permitiendo a los usuarios realizar pedidos según su tipo (cliente, administrador, barista, etc.), visualizar el historial de órdenes y administrar el negocio en un sistema robusto y escalable.

## Características principales

- Autenticación y gestión de usuarios con roles diferenciados:
  - Clientes: pueden realizar pedidos y ver su historial.
  - Administradores: gestionan productos, usuarios y pedidos.
  - Baristas: visualizan y gestionan las órdenes a preparar.
- Creación y administración de productos del menú (cafés, postres, etc.).
- Sistema de pedidos online: selección de productos, confirmación y seguimiento.
- Panel de administración seguro y amigable.
- Historial de órdenes para usuarios.
- Interfaz web responsiva y atractiva.
- Código limpio y modular siguiendo las buenas prácticas de Django.

## Tecnologías utilizadas

- **Backend:** [Django](https://www.djangoproject.com/) (Python)
- **Frontend:** HTML5, CSS3, Django Templates
- **Base de datos:** SQLite (por defecto, fácil de cambiar a PostgreSQL/MySQL)
- **Otros:** Bootstrap (opcional), autenticación integrada de Django

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/esjuanbravo/coffee_shop_app.git
   cd coffee_shop_app
   ```

2. **Crear y activar un entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos y migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario**

   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

7. **Abrir en el navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Estructura del proyecto

```
coffee_shop_app/
├── manage.py
├── coffee_shop_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
├── users/
│   ├── models.py
│   ├── views.py
│   └── ...
├── static/
│   └── ...
└── templates/
    └── ...
```

## Uso

- Los usuarios deben registrarse o iniciar sesión para realizar pedidos.
- Los administradores pueden agregar, editar o eliminar productos y gestionar usuarios desde el panel `/admin/`.
- Los baristas visualizan los pedidos pendientes en su panel personalizado.

## Capturas de pantalla

> Agrega aquí imágenes de la interfaz en producción (login, panel de pedidos, menú, etc.).

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un Issue o un Pull Request para sugerir mejoras o reportar errores.

1. Haz un fork del repositorio.
2. Crea una rama: `git checkout -b mi-feature`
3. Realiza tus cambios y haz commit: `git commit -am 'Agrega nueva feature'`
4. Haz push a la rama: `git push origin mi-feature`
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

## Autor

- [esjuanbravo](https://github.com/esjuanbravo)

---

> Proyecto desarrollado como ejemplo de sistema escalable con Django para cafeterías.
