import ray

@ray.remote
def es_par(numero):
    return "par" if numero % 2 == 0 else "impar"
