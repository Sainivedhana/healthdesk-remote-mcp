from fastmcp import FastMCP

mcp = FastMCP("Healthdesk Remote Server")


@mcp.tool
def get_health_tips() -> str:
    """Provide general health tips for patients."""
    return (
        "Healthdesk tip: Stay hydrated, eat balanced meals, "
        "get enough sleep, and maintain regular physical activity."
    )


@mcp.tool
def get_specialization_info(specialization: str) -> str:
    """Explain what type of doctor handles a medical specialization."""

    specializations = {
        "cardiology": "A cardiologist specializes in heart and cardiovascular conditions.",
        "dermatology": "A dermatologist specializes in skin, hair, and nail conditions.",
        "pediatrics": "A pediatrician provides medical care for children.",
        "orthopedics": "An orthopedic doctor treats bones, joints, muscles, and related conditions.",
        "dentistry": "A dentist specializes in oral health, teeth, and gums.",
    }

    return specializations.get(
        specialization.lower(),
        f"Healthdesk does not currently have information about {specialization}."
    )


@mcp.tool
def get_appointment_guidelines() -> str:
    """Provide general appointment booking guidelines."""

    return (
        "To book an appointment, you need a patient ID, "
        "doctor ID, appointment date, appointment time, and reason for the visit."
    )

app = mcp.http_app(stateless_http=True)
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
