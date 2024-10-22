from scr.logica.calculos import Calculadora, NoSePuedeCalcular


def ejecutar():
    try:
        # Preguntar cuántos números se van a ingresar
        n = int(input("¿Cuántos números desea ingresar? "))

        if n <= 0:
            raise ValueError("El número de elementos debe ser mayor a cero.")

        # Ingresar los números uno por uno
        numeros = []
        for i in range(n):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

        # Crear la instancia de la calculadora
        calculadora = Calculadora(numeros)
        media = calculadora.media()
        desviacion_estandar = calculadora.desviacion_estandar()

        # Mostrar los resultados
        print(f"Media: {media}")
        print(f"Desviación Estándar: {desviacion_estandar}")

    except ValueError as e:
        print(f"Error: {e}")
    except NoSePuedeCalcular as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    ejecutar()