from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def instructores(request):
    data = {
        'titulo': 'Instructores',
        'capacitacion': [
            {'nombre': 'Linus Torvalds', 'imagen1': 'imagenes/Instructor1.jpg', 'imagen2': 'imagenes/instructor2.jpg', 'especialidad': 'Sistemas Operativos y Software de Código Abierto', 'descripcion': 'Linus Torvalds es el creador del sistema operativo Linux, uno de los pilares del software de código abierto. Su trabajo en el desarrollo del núcleo Linux ha tenido un impacto significativo en la informática moderna, incluyendo servidores, dispositivos móviles y supercomputadoras. Torvalds sigue siendo una figura clave en la comunidad de código abierto y en el desarrollo de sistemas operativos.'},
            {'nombre': 'Grace Hopper', 'imagen1': 'imagenes/Instructor3.jpg', 'imagen2': 'imagenes/instructor4.jpg', 'especialidad': 'Lenguajes de Programación y Compiladores', 'descripcion': 'Grace Hopper fue una pionera en el desarrollo de lenguajes de programación y compiladores. Es conocida por su trabajo en el desarrollo del lenguaje COBOL y por la creación de uno de los primeros compiladores. Hopper tuvo un impacto duradero en la informática, facilitando la creación de programas complejos y accesibles para la programación empresarial.'},
            {'nombre': 'Donald Knuth', 'imagen1': 'imagenes/Instructor5.webp', 'imagen2': 'imagenes/instructor6.avif', 'especialidad': 'Algoritmos y Teoría de la Computación', 'descripcion': 'Donald Knuth es un influyente informático conocido por su obra monumental, "The Art of Computer Programming". Knuth ha hecho contribuciones significativas a la teoría de algoritmos y estructuras de datos, y su trabajo ha sentado las bases para el desarrollo de técnicas avanzadas en la informática. Su enfoque riguroso y detallado en el análisis y la optimización de algoritmos ha sido esencial para el avance de la ciencia de la computación.'}
        ]
    }
    return render(request, 'informacion.html', data)

def curso(request):
    data = {
        'titulo': 'curso',
        'capacitacion': [
            {'nombre': 'Desarrollo Web con Django', 'imagen1': 'imagenes/Curso1', 'imagen2': 'imagenes/Curso2', 'duracion': '8 semanas', 'Reseña': 'Este curso te introduce al framework Django, cubriendo desde los fundamentos básicos hasta técnicas avanzadas para el desarrollo de aplicaciones web robustas y escalables. Aprenderás a trabajar con modelos, vistas y plantillas, así como a implementar autenticación de usuarios y formularios. Al finalizar, serás capaz de construir aplicaciones web completas y funcionales utilizando las mejores prácticas del desarrollo en Django.'},
            {'nombre': 'Introducción a Python para Ciencia de Datos', 'imagen3': 'imagenes/Curso3', 'imagen4': 'imagenes/Curso4', 'duracion': '6 semanas', 'reseña': 'Este curso está diseñado para principiantes en el campo de la ciencia de datos. Aprenderás los fundamentos de Python, cómo manejar datos utilizando bibliotecas como Pandas y NumPy, y cómo visualizar datos con Matplotlib y Seaborn. El curso cubre técnicas esenciales de análisis y manipulación de datos, preparándote para comenzar a trabajar en proyectos de ciencia de datos y análisis estadístico.'},
            {'nombre': 'Diseño de Interfaces de Usuario con React', 'imagen5': 'imagenes/Curso5', 'imagen6': 'imagenes/Curso6', 'duracion': '10 semanas', 'Reseña': 'En este curso, explorarás el desarrollo de interfaces de usuario modernas utilizando React. Desde la creación de componentes hasta la gestión del estado con hooks, aprenderás a construir aplicaciones web interactivas y reactivas. El curso incluye prácticas en el uso de Redux para el manejo del estado global y la integración de APIs para obtener datos dinámicos. Ideal para aquellos que buscan especializarse en el diseño de experiencias de usuario en el entorno web.'}
        ]
    }
    return render(request, 'informacion.html', data)

def egresados(request):
    data = {
        'titulo': 'egresados',
        'capacitacion': [
            {'nombre': 'Jeff Dean', 'imagen1': 'imagenes/Egresado1', 'imagen2': 'imagenes/Egresado2', 'Nombre de la empresa': 'Google (Senior Fellow)', 'Opinion': 'Jeff Dean, Senior Fellow en Google, ha utilizado su educación en ingeniería informática para hacer contribuciones significativas a la infraestructura de Google y a la investigación en aprendizaje automático. Destaca cómo su formación en algoritmos y sistemas ha sido esencial para desarrollar tecnologías escalables y eficaces. Aprecia la educación que recibió por proporcionarle una base sólida en teoría y práctica, que ha sido crucial para su carrera en una de las empresas tecnológicas más grandes del mundo.'},
            {'nombre': 'Marissa Mayer', 'imagen3': 'imagenes/Egresado3', 'imagen4': 'imagenes/Egresado4', 'Nombre de la empresa': 'Yahoo! (Ex CEO)', 'Opinion': 'Marissa Mayer, ex CEO de Yahoo! y ex vicepresidenta de Google, resalta cómo su formación en ingeniería informática le ha permitido desarrollar una carrera destacada en la tecnología. Destaca cómo sus estudios le proporcionaron una sólida base en algoritmos y sistemas que fueron fundamentales para su trabajo en Google y Yahoo!, donde lideró equipos en el desarrollo de productos innovadores y mejoras en la experiencia del usuario. Aprecia la educación técnica que recibió por prepararla para enfrentar desafíos complejos y liderar en el campo de la tecnología.'},
            {'nombre': 'Margaret Hamilton', 'imagen5': 'imagenes/Egresado5', 'imagen6': 'imagenes/Egresado6', 'Nombre de la empresa': 'Hamilton Technologies (Fundadora y CEO)', 'Opinion': 'Margaret Hamilton, conocida por su trabajo en el desarrollo del software de navegación del Apollo 11, destaca cómo su formación en ingeniería informática le permitió liderar el desarrollo de sistemas críticos para la misión lunar. Valora la educación técnica que recibió por su enfoque en la resolución de problemas complejos y el desarrollo de software robusto. Su experiencia ha sido fundamental en su éxito como innovadora y líder en el campo de la ingeniería informática.'}
        ]
    }
    return render(request, 'informacion.html', data)