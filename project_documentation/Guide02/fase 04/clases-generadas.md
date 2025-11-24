# Clases Generadas — Modelos de Base de Datos

El sistema utiliza **SQLAlchemy ORM** para mapear las entidades del negocio a tablas de la base de datos MySQL. A continuación se presentan las **clases generadas** que representan el modelo de datos.

---

## 1. Clase `Usuario`

**Descripción:**  
Representa a los usuarios del sistema (estudiantes y administradores).

**Atributos:**
- `id` (Integer, Primary Key): Identificador único del usuario.
- `correo` (String, Unique, Index): Correo institucional del usuario.
- `password_hash` (String): Contraseña del usuario (almacenada en texto plano en prototipo; en producción debe usar hash).
- `rol` (String): Rol del usuario (`student` o `admin`).

**Relaciones:**
- `reservas` (One-to-Many): Un usuario puede tener múltiples reservas.

**Archivo:** `backend/models/user.py`
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    rol = Column(String(20))

    reservas = relationship("Reserva", back_populates="usuario")
```

---

## 2. Clase `Reserva`

**Descripción:**  
Representa una reserva realizada por un usuario.

**Atributos:**
- `id` (Integer, Primary Key): Identificador único de la reserva.
- `usuario_id` (Integer, Foreign Key): ID del usuario que realizó la reserva.
- `fecha` (Date, Index): Fecha de la reserva.
- `hora_inicio` (String): Hora de inicio de la franja (formato `HH:MM`).
- `hora_fin` (String): Hora de fin de la franja (formato `HH:MM`).
- `estado` (String): Estado de la reserva (`reservado` o `cancelado`).

**Relaciones:**
- `usuario` (Many-to-One): Una reserva pertenece a un usuario.

**Archivo:** `backend/models/reserva.py`
```python
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from backend.database.database import Base
from sqlalchemy.orm import relationship

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(Date, index=True)
    hora_inicio = Column(String(10))
    hora_fin = Column(String(10))
    estado = Column(String(20), default="reservado")

    usuario = relationship("Usuario", back_populates="reservas")
```

---

## 3. Clase `Bloqueo`

**Descripción:**  
Representa un bloqueo administrativo del calendario (día completo o franja específica).

**Atributos:**
- `id` (Integer, Primary Key): Identificador único del bloqueo.
- `fecha` (Date, Index): Fecha del bloqueo.
- `hora_inicio` (String, Nullable): Hora de inicio (null para bloqueo de día completo).
- `hora_fin` (String, Nullable): Hora de fin (null para bloqueo de día completo).
- `tipo` (String): Tipo de bloqueo (`dia` o `franja`).

**Archivo:** `backend/models/bloqueo.py`
```python
from sqlalchemy import Column, Integer, String, Date
from backend.database.database import Base

class Bloqueo(Base):
    __tablename__ = "bloqueos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    hora_inicio = Column(String(10), nullable=True)
    hora_fin = Column(String(10), nullable=True)
    tipo = Column(String(10))
```

---

## Diagrama de Relaciones
```
┌──────────────┐
│   Usuario    │
├──────────────┤
│ id (PK)      │
│ correo       │
│ password_hash│
│ rol          │
└──────┬───────┘
       │ 1
       │
       │ N
┌──────▼───────┐
│   Reserva    │
├──────────────┤
│ id (PK)      │
│ usuario_id(FK│
│ fecha        │
│ hora_inicio  │
│ hora_fin     │
│ estado       │
└──────────────┘

┌──────────────┐
│   Bloqueo    │
├──────────────┤
│ id (PK)      │
│ fecha        │
│ hora_inicio  │
│ hora_fin     │
│ tipo         │
└──────────────┘
```

---

## Tablas Generadas en MySQL

Al ejecutar la aplicación, SQLAlchemy crea automáticamente las siguientes tablas en la base de datos:

**Tabla `usuarios`:**
```sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    rol VARCHAR(20),
    INDEX idx_correo (correo)
);
```

**Tabla `reservas`:**
```sql
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha DATE NOT NULL,
    hora_inicio VARCHAR(10),
    hora_fin VARCHAR(10),
    estado VARCHAR(20) DEFAULT 'reservado',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    INDEX idx_fecha (fecha)
);
```

**Tabla `bloqueos`:**
```sql
CREATE TABLE bloqueos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora_inicio VARCHAR(10),
    hora_fin VARCHAR(10),
    tipo VARCHAR(10),
    INDEX idx_fecha (fecha)
);
```

---

## Conclusión

Las clases generadas representan fielmente el modelo conceptual definido en la Fase 03. La implementación con SQLAlchemy facilita la manipulación de datos y garantiza la integridad referencial entre usuarios, reservas y bloqueos.
