import ray
from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel
from core.tasks import es_par

Serve.start(detached=True)

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

serve.run(MLModelService.bind())

