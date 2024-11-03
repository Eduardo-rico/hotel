from pydantic import BaseModel

from typing import Literal
from pydantic import BaseModel, Field

class CustomerInput(BaseModel):
    age: int = Field(..., ge=0, le=100)
    annual_income: float = Field(..., ge=0, le=500000)
    num_bookings_per_year: int = Field(..., ge=0, le=50)
    avg_spend_per_booking: float = Field(..., ge=0, le=100000)
    travel_frequency: int = Field(..., ge=1, le=12)
    avg_stay_duration: int = Field(..., ge=1, le=15)
    tech_usage_level: int = Field(..., ge=0, le=10)
    loyalty_program_frequency: int = Field(..., ge=0, le=50)
    distance_from_home: int = Field(..., ge=10, le=5000)
    num_rooms: int = Field(..., ge=1, le=5)
    travel_purpose: Literal['business', 'leisure', 'mixed']
    accommodation_preference: Literal['luxury_hotel', 'mid_range_hotel', 'hostel']
    travels_with_family: Literal['yes', 'no']
    main_activity: Literal['work', 'relaxation', 'tourism', 'shopping']
    room_type: Literal['single', 'double', 'suite']
    requires_transport: Literal['yes', 'no']
