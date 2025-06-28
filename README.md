# 📚 Blog de Libros en Inglés

Este es un proyecto de blog desarrollado con Django. Permite a los usuarios registrados publicar reseñas de libros en inglés, comentar, editar sus propios comentarios y gestionar sus publicaciones.

## 🚀 Funcionalidades

- Registro, inicio y cierre de sesión.
- Edición de perfil con avatar.
- Crear, editar y eliminar publicaciones.
- Comentar publicaciones.
- Editar y eliminar tus propios comentarios.
- Buscador de publicaciones por título o contenido.
- Paginación de publicaciones.
- Editor enriquecido para los contenidos (CKEditor).
- Diseño responsive con Bootstrap 5.
- Sistema de mensajes para acciones del usuario.

## 🛠️ Tecnologías utilizadas

- Python 3.13
- Django 4.x
- SQLite (por defecto)
- Bootstrap 5
- CKEditor (django-ckeditor)

## 📸 Capturas

_(Agregá screenshots del blog, formulario de publicación, comentarios, etc.)_

## 🧪 Instalación local

```bash
git clone https://github.com/tu-usuario/blog-libros.git
cd blog-libros
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
