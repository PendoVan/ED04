# Pantallas de Interfaz de Usuario

A continuación se presentan las capturas de pantalla de las principales interfaces del **Sistema de Reservas de Canchas FISI**.

---

## 1. Pantalla de Login

**Descripción:**  
Permite a los usuarios (estudiantes y administradores) iniciar sesión con su correo institucional y contraseña.

**Funcionalidades:**
- Validación de correo institucional (`@unmsm.edu.pe`).
- Redirección según rol: estudiantes a `reservas.html`, administradores a `admin_dashboard.html`.

<img width="1600" height="887" alt="image" src="https://github.com/user-attachments/assets/f5ed85db-b94f-43d5-8bb1-b8d887d61446" />


---

## 2. Pantalla de Registro

**Descripción:**  
Permite a los estudiantes crear una cuenta con su correo institucional.

**Funcionalidades:**
- Validación de dominio `@unmsm.edu.pe`.
- Creación de usuario con rol `student`.

<img width="611" height="636" alt="image" src="https://github.com/user-attachments/assets/ad75e973-f57f-4968-94d9-756a109ce500" />


---

## 3. Pantalla de Reservas (Estudiante)

**Descripción:**  
Muestra el calendario de disponibilidad y permite seleccionar una franja horaria para reservar.

**Funcionalidades:**
- Selección de fecha.
- Visualización de franjas disponibles en un selector (`<select>`).
- Validación automática de topes semanales, solapamientos y bloqueos.
- Confirmación de reserva.

<img width="1600" height="820" alt="image" src="https://github.com/user-attachments/assets/e0ff8799-c5e3-4ce9-99c3-8ddc5a198087" />


---

## 4. Pantalla de Mis Reservas (Estudiante)

**Descripción:**  
Lista las reservas activas del estudiante y permite cancelarlas.

**Funcionalidades:**
- Ver detalles de cada reserva (fecha, hora de inicio, hora de fin).
- Cancelar reserva con confirmación.

<img width="1600" height="814" alt="image" src="https://github.com/user-attachments/assets/db65c588-d122-4075-af4c-d1f609b1aab4" />


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

<img width="1600" height="842" alt="image" src="https://github.com/user-attachments/assets/f61cacb8-b24b-4cc5-90e3-2744cf0798fc" />


---

## 6. Detalle de Disponibilidad (Admin)

**Descripción:**  
Tabla que muestra el estado de cada franja horaria para una fecha específica.

**Estados:**
- **Disponible** (verde)
- **Reservado** (rojo)
- **Bloqueado** (gris)

<img width="722" height="766" alt="image" src="https://github.com/user-attachments/assets/49c906f9-501b-4b9b-ac16-10cabe65d316" />


---

## 7. Gestión de Bloqueos (Admin)

**Descripción:**  
Permite registrar y eliminar bloqueos del calendario.

**Funcionalidades:**
- Selección de fecha.
- Selección de franja horaria (para bloqueo de franja específica).
- Confirmación de bloqueo.
- Listado de bloqueos activos con opción de eliminar.

<img width="736" height="774" alt="image" src="https://github.com/user-attachments/assets/87ee5c0a-b8da-4e08-b380-8f405403a483" />

---

## Notas Técnicas

- Las interfaces fueron desarrolladas con **HTML5, CSS3 y JavaScript Vanilla**.
- El diseño utiliza la fuente **Inter** y una paleta de colores moderna basada en **Tailwind CSS** (variables CSS personalizadas).
- La comunicación con el backend se realiza mediante `fetch` (API REST).
- El sistema es **mobile-friendly** y se adapta a diferentes tamaños de pantalla.

---

## Conclusión

Las pantallas de interfaz cumplen con los requisitos de usabilidad definidos en los **RNF-1** (interfaz clara con colores, mobile-friendly). Todas las funcionalidades críticas están implementadas y son accesibles desde una interfaz intuitiva.

