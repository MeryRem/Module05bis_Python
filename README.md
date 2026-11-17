ex3.
Como elegir ruta absoluta o relativa a la hora de importar:
-El archivo está fuera del paquete? → absoluta
-Está dentro y cerca? → relativa (. misma carpeta, .. carpeta de arriba)
-Dudas? → absoluta

ex4
el spellbook necesita al validator para decidir si el hechizo vale.
el validator necesita al spellbook para saber qué ingredientes están permitidos.

ft_kaboom_1.py:
El import va después de los print para que se vea el título antes del error. El # noqa: E402 evita que flake8 se queje por eso
