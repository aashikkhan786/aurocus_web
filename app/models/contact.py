"""Contact form Pydantic models."""

import re
from pydantic import BaseModel, field_validator


class ContactInquiry(BaseModel):
    """Model for contact form submissions."""

    full_name: str
    business_email: str
    company_name: str
    country: str
    service_interested: str
    project_details: str

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Full name must be at least 2 characters.")
        return v

    @field_validator("business_email")
    @classmethod
    def validate_business_email(cls, v: str) -> str:
        v = v.strip()
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, v):
            raise ValueError("Please enter a valid email address.")
        return v

    @field_validator("company_name")
    @classmethod
    def validate_company_name(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Company name must be at least 2 characters.")
        return v

    @field_validator("country")
    @classmethod
    def validate_country(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Please select a country.")
        return v

    @field_validator("service_interested")
    @classmethod
    def validate_service_interested(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Please select a service.")
        return v

    @field_validator("project_details")
    @classmethod
    def validate_project_details(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 10:
            raise ValueError("Project details must be at least 10 characters.")
        return v


class ContactResponse(BaseModel):
    """Response model for contact form API responses."""

    success: bool
    message: str
    inquiry_id: int | None = None
