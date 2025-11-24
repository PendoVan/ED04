# Software  
En esta sección se detallan las herramientas reales utilizadas durante el desarrollo del **Sistema de Reservas de Canchas FISI**, desde el análisis hasta la codificación, pruebas y documentación.

---

## 1. Sistema Operativo utilizado
El desarrollo se realizó en un equipo con:

- **Windows 10 / Windows 11**  
- Terminales utilizadas: PowerShell, CMD y Git Bash  
- Compatibilidad con GitHub Codespaces

---

## 2. Software de Desarrollo Backend

### **Lenguaje**
- **Python 3.12+**

### **Framework principal**
- **FastAPI**  
  Utilizado para crear la API REST del sistema.

### **Servidor de aplicación**
- **Uvicorn**  
  Ejecutado mediante:  

  uvicorn app.main:app --reload


### **ORM**
- **Prisma ORM (Python)**  
Usado para la conexión y manipulación de la base de datos MySQL.

### **Dependencias reales detectadas en el proyecto**
Según la carpeta `backend/app`:

- `fastapi`
- `pydantic`  
- `pydantic-settings`
- `email-validator`
- `prisma`
- `uvicorn`
- `python-dotenv`
- `python-multipart`

---

## 3. Software de Base de Datos

### **Motor utilizado**
- **MySQL 8.x**

### **Herramientas utilizadas**
- **MySQL Workbench**  
Para pruebas, verificaciones, consultas SQL y modelado básico.

### **Archivos reales de BD**
- `schema.prisma`  
- Migraciones en la carpeta `/prisma/migrations`

---

## 4. Software de Desarrollo Frontend

### **Estructura usada**
El frontend está en la carpeta `/frontend` y contiene:

- **HTML5**
- **CSS3**
- **JavaScript Vanilla**

### **Herramientas utilizadas**
- **Live Server** (VSCode)  
Para visualizar el frontend durante pruebas.

- **GitHub Codespaces**  
Para preview del frontend cuando se trabaja remoto.

---

## 5. Herramientas de Control de Versiones y Repositorio

- **Git**  
Utilizado para el control de versiones del proyecto.

- **GitHub**  
Repositorio oficial:  
https://github.com/PendoVan/ED04

- Uso de **Branches**, commits y sincronización con Codespaces.

---

## 6. Software de Modelado, Diseño y Documentación

### **Modelado de procesos**
- **Bizagi Modeler**  
Usado para diagramas BPMN (proceso principal y subprocesos).

### **Diagramado y arquitectura**
- **Draw.io / diagrams.net**  
- **Canva**  
Para patrones de arquitectura, diagramas estéticos y material visual.

### **Documentación**
- **Markdown (VSCode)**  
- Carpetas de fases estructuradas en `/fases01-06`

---

## 7. Servicios Externos

### **Notificaciones**
- **SMTP (Outlook / UNMSM)**  
Para el envío de correos de confirmación (aún en fase de integración).

### **Exposición del backend**
- **Cloudflare Tunnel** *(opcional usado en pruebas)*  
Para exponer el backend temporalmente sin abrir puertos.

---

## 8. Software adicional utilizado
- **WSL2 (opcional)**  
- **Node.js** *(solo para Prisma CLI cuando necesario)*  
- **Navegadores modernos:**  
- Google Chrome  
- Firefox  

---

## Conclusión
El software utilizado permite un desarrollo completo y moderno, basado en **FastAPI + Prisma + MySQL** y soportado por herramientas profesionales como VSCode, GitHub y Bizagi.  
Este stack tecnológico es estable, escalable y adecuado para el alcance del proyecto académico.
