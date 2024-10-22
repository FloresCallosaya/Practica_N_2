from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal con menú de opciones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return render_template('resultado.html', tipo='Inscripción', datos={'Nombre': nombre, 'Apellido': apellido, 'Curso': curso})
    return render_template('inscripcion.html')

# Ruta para el formulario de registro de usuarios
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return render_template('resultado.html', tipo='Registro de Usuario', datos={'Nombre': nombre, 'Apellido': apellido, 'Correo': correo})
    return render_template('registro_usuario.html')

# Ruta para el formulario de registro de productos
@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('resultado.html', tipo='Registro de Producto', datos={'Producto': producto, 'Categoría': categoria, 'Existencia': existencia, 'Precio': precio})
    return render_template('registro_producto.html')

# Ruta para el formulario de registro de libros
@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        tipo_medio = request.form['tipo_medio']
        return render_template('resultado.html', tipo='Registro de Libro', datos={'Título': titulo, 'Autor': autor, 'Resumen': resumen, 'Tipo de Medio': tipo_medio})
    return render_template('registro_libro.html')

if __name__ == "__main__":
    app.run(debug=True)
