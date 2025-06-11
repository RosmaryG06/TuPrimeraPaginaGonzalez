# Mi Blog en Django

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPO>
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicia el servidor:
   ```
   python manage.py runserver
   ```

## Orden para probar la funcionalidad

1. **Crear un autor**: Navega a "Nuevo Autor" y carga un autor.
2. **Crear una categoría**: Ve a "Nueva Categoría" y agrega una categoría.
3. **Crear un post**: Ve a "Nuevo Post" y crea un post usando el autor y la categoría que creaste antes.
4. **Ver posts**: En "Ver Posts" encontrarás el listado.
5. **Buscar posts**: En "Buscar Post" puedes buscar por título.

**La herencia de plantillas está implementada en todos los HTML con `base.html` como plantilla base.**

---

¡Listo! Sube todo a GitHub y tendrás una entrega completa y funcional. ¿Te ayudo con algún detalle específico?