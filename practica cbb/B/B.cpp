#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void es_ordenable(vector<int>& a, vector<int>& b, vector<pair<int, int>>& r) {
    for (auto& valores : r) {
        int inicio = valores.first - 1;  // Convertir a índice base 0
        int fin = valores.second;        // Python usa [inicio:fin), C++ necesita fin-1
        
        // Crear subvectores
        vector<int> subA(a.begin() + inicio, a.begin() + fin);
        vector<int> subB(b.begin() + inicio, b.begin() + fin);
        
        // Crear copias ordenadas para comparar
        vector<int> subA_ordenado = subA;
        vector<int> subB_ordenado = subB;
        sort(subA_ordenado.begin(), subA_ordenado.end());
        sort(subB_ordenado.begin(), subB_ordenado.end());
        
        // Verificar si ambos subarreglos están ordenados
        if (subA == subA_ordenado && subB == subB_ordenado) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

int main() {
    int longitud;
    cin >> longitud;
    
    vector<int> A(longitud);
    for (int i = 0; i < longitud; i++) {
        cin >> A[i];
    }
    
    vector<int> B(longitud);
    for (int i = 0; i < longitud; i++) {
        cin >> B[i];
    }
    
    int consultas;
    cin >> consultas;
    
    vector<pair<int, int>> rangos(consultas);
    for (int i = 0; i < consultas; i++) {
        cin >> rangos[i].first >> rangos[i].second;
    }
    
    es_ordenable(A, B, rangos);
    
    return 0;
}