#Valdez Lopez Juan Manuel 

#Metodo de la secante en Python

def f(x):
    return x**3 - x - 2  # Cambia esto por tu función

def secante(f, x0, x1, tol=1e-8, max_iter=50):
    print(f"{'Iter':>5} {'x0':>18} {'x1':>18} {'x2':>18} {'f(x2)':>12} {'Error':>12}")
    print("-" * 90)
    
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        
        if abs(f1 - f0) < 1e-14:
            print("Division por cero: f(x1) - f(x0) ≈ 0")
            break
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        fx2 = f(x2)
        error = abs(x2 - x1)
        
        print(f"{i+1:>5} {x0:>18.10f} {x1:>18.10f} {x2:>18.10f} {fx2:>12.2e} {error:>12.2e}")
        
        if error < tol:
            print(f"\n✓ Convergio en {i+1} iteraciones")
            return x2
        
        x0 = x1
        x1 = x2
    
    print(f"\nADVERTENCIA: Se alcanzo el maximo de iteraciones ({max_iter})")
    return x1


#Parametros
x0 = 1.0
x1 = 2.0
tolerancia = 1e-8
max_iteraciones = 50

raiz = secante(f, x0, x1, tolerancia, max_iteraciones)
print(f"Raiz aproximada: {raiz:.10f}")
print(f"f(raiz) = {f(raiz):.2e}")