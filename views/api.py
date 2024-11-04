from fastapi import APIRouter
from models.customer_model import CustomerInput
from controllers.customer_controller import predict_customer_type

router = APIRouter()


customer_type_mapping = {
    0: 'bleisure_traveler',
    1: 'business_traveler',
    2: 'luxury_family_couple',
    3: 'millennial_lifestyle'
}

@router.options("/predict")
def options():
    return {"Allow": "POST, OPTIONS"}


@router.post("/predict")
def predict(customer: CustomerInput):
    prediction = predict_customer_type(customer)
    customer_type = customer_type_mapping[int(prediction[0])]  
    return {"customer_type": customer_type}


@router.get("/ok")
def ok():
    return {"message": "ok"}
