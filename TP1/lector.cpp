#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct datospersona {
    int id_registro;
    int edad;
    int cedula;
    float peso;
    float altura;
    string genero;
    string nombre;
};

int main() {
    int registro_buscado;
    cout << "Ingrese el numero de registro que desea consultar: ";
    cin >> registro_buscado;

    fstream archivo_binario("personas.dat", ios::in | ios::binary);

    if (!archivo_binario.is_open()) {
        cout << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    datospersona persona;
    archivo_binario.seekg((registro_buscado - 1) * sizeof(datospersona), ios::beg); // Posicionamos el puntero del archivo
    archivo_binario.read(reinterpret_cast<char*>(&persona), sizeof(datospersona));

    if (archivo_binario.fail()) {
        cout << "Registro no encontrado." << endl;
    } else {
        cout << "Datos de la persona:\n";
        cout << "ID: " << persona.id_registro << endl;
        cout << "Nombre: " << persona.nombre << endl;
        cout << "Edad: " << persona.edad << endl;
        cout << "Cedula: " << persona.cedula << endl;
        cout << "Peso: " << persona.peso << endl;
        cout << "Altura: " << persona.altura << endl;
        cout << "Genero: " << persona.genero << endl;   
    }

    archivo_binario.close();
    return 0;
}