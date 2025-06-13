#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

string es_triangular(long long num) {
    double resultado = (-1 + sqrt(1 + 8.0 * num)) / 2.0;
    if (resultado == floor(resultado)) {
        return "SI";
    } else {
        return "NO";
    }
}

int main() {
    int cantidad;
    cin >> cantidad;

    vector<long long> numeros(cantidad);
    for (int i = 0; i < cantidad; ++i) {
        cin >> numeros[i];
    }

    for (int i = 0; i < cantidad; ++i) {
        cout << es_triangular(numeros[i]) << endl;
    }

    return 0;
}
