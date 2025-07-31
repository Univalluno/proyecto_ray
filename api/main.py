import ray
from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel
from core.tasks import es_par

ray.init()
serve.start(detached=True)

app = FastAPI()

class NumberInput(BaseModel):
    number: int

@serve.deployment
@serve.ingress(app)
class MLModelService:
    @app.post("/predict")
    async def predict(self, item: NumberInput):
        result = await es_par.remote(item.number)
        return {"resultado": result}

# Lanza el servicio (sin host ni port)
serve.run(MLModelService.bind())

