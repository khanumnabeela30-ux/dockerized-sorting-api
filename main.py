from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SortRequest(BaseModel):
    numbers: list[int]
    algorithm: str

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

@app.post("/sort")
def sort_numbers(request: SortRequest):
    if request.algorithm.lower() == "bubble":
        return {"sorted_list": bubble_sort(request.numbers)}
    else:
        return {"error": "Only bubble sort is supported"}
