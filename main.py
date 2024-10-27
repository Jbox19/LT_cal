from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculator")
def cal(a: float, b: float, operation: str):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'")
    
    return {"operation": operation, "a": a, "b": b, "result": result}
