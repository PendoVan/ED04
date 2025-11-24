# Pantallas de Interfaz de Usuario

A continuación se presentan las capturas de pantalla de las principales interfaces del **Sistema de Reservas de Canchas FISI**.

---

## 1. Pantalla de Login

**Descripción:**  
Permite a los usuarios (estudiantes y administradores) iniciar sesión con su correo institucional y contraseña.

**Funcionalidades:**
- Validación de correo institucional (`@unmsm.edu.pe`).
- Redirección según rol: estudiantes a `reservas.html`, administradores a `admin_dashboard.html`.

![Pantalla de Login](./screenshots/login.png)

---

## 2. Pantalla de Registro

**Descripción:**  
Permite a los estudiantes crear una cuenta con su correo institucional.

**Funcionalidades:**
- Validación de dominio `@unmsm.edu.pe`.
- Creación de usuario con rol `student`.

![Pantalla de Registro](./screenshots/registro.png)

---

## 3. Pantalla de Reservas (Estudiante)

**Descripción:**  
Muestra el calendario de disponibilidad y permite seleccionar una franja horaria para reservar.

**Funcionalidades:**
- Selección de fecha.
- Visualización de franjas disponibles en un selector (`<select>`).
- Validación automática de topes semanales, solapamientos y bloqueos.
- Confirmación de reserva.

![Pantalla de Reservas](./screenshots/reservas.png)

---

## 4. Pantalla de Mis Reservas (Estudiante)

**Descripción:**  
Lista las reservas activas del estudiante y permite cancelarlas.

**Funcionalidades:**
- Ver detalles de cada reserva (fecha, hora de inicio, hora de fin).
- Cancelar reserva con confirmación.

![Pantalla de Mis Reservas](./screenshots/mis_reservas.png)

---

## 5. Panel de Administración (Consejero)

**Descripción:**  
Interfaz para gestionar bloqueos del calendario y consultar disponibilidad.

**Funcionalidades:**
- **Gestión de bloqueos:**
  - Ver bloqueos existentes de una fecha.
  - Bloquear día completo.
  - Bloquear franja específica.
  - Eliminar bloqueos.
- **Consulta de disponibilidad:**
  - Ver el estado de todas las franjas de una fecha (disponible, reservado, bloqueado).

![Panel de Administración](./screenshots/admin_dashboard.png)

---

## 6. Detalle de Disponibilidad (Admin)

**Descripción:**  
Tabla que muestra el estado de cada franja horaria para una fecha específica.

**Estados:**
- **Disponible** (verde)
- **Reservado** (rojo)
- **Bloqueado** (gris)

![Disponibilidad Admin](./screenshots/disponibilidad_admin.png)

---

## 7. Gestión de Bloqueos (Admin)

**Descripción:**  
Permite registrar y eliminar bloqueos del calendario.

**Funcionalidades:**
- Selección de fecha.
- Selección de franja horaria (para bloqueo de franja específica).
- Confirmación de bloqueo.
- Listado de bloqueos activos con opción de eliminar.

![Gestión de Bloqueos](./screenshots/bloqueos.png)

---

## Notas Técnicas

- Las interfaces fueron desarrolladas con **HTML5, CSS3 y JavaScript Vanilla**.
- El diseño utiliza la fuente **Inter** y una paleta de colores moderna basada en **Tailwind CSS** (variables CSS personalizadas).
- La comunicación con el backend se realiza mediante `fetch` (API REST).
- El sistema es **mobile-friendly** y se adapta a diferentes tamaños de pantalla.

---

## Conclusión

Las pantallas de interfaz cumplen con los requisitos de usabilidad definidos en los **RNF-1** (interfaz clara con colores, mobile-friendly). Todas las funcionalidades críticas están implementadas y son accesibles desde una interfaz intuitiva.
