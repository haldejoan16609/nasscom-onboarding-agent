# NASSCOM Employee Onboarding Agent

employees = {
    "EMP001": {
        "name": "Amit Sharma",
        "compliance": "Compliant",
        "provisioning": True
    },
    "EMP002": {
        "name": "Priya Patel",
        "compliance": "Pending",
        "provisioning": False
    }
}


def get_employee_profile_id(employee_id):
    """Retrieve the employee profile ID."""
    if employee_id in employees:
        return employee_id
    return None


def check_compliance(profile_id):
    """Check the employee's compliance status."""
    return employees[profile_id]["compliance"]


def check_provisioning(profile_id):
    """Check whether required provisioning exists."""
    return employees[profile_id]["provisioning"]


def send_notification(employee_name, message):
    """Simulate sending an onboarding notification."""
    print(f"Notification for {employee_name}: {message}")


def onboard_employee(employee_id):
    """Run the employee onboarding workflow."""

    profile_id = get_employee_profile_id(employee_id)

    if not profile_id:
        print("Employee profile not found.")
        return

    employee = employees[profile_id]
    compliance = check_compliance(profile_id)
    provisioning = check_provisioning(profile_id)

    print(f"\nEmployee: {employee['name']}")
    print(f"Profile ID: {profile_id}")
    print(f"Compliance: {compliance}")
    print(f"Provisioning: {provisioning}")

    if compliance != "Compliant":
        send_notification(
            employee["name"],
            "Onboarding cannot proceed. Compliance is not complete."
        )
        return

    if not provisioning:
        send_notification(
            employee["name"],
            "Onboarding cannot proceed. Required provisioning is missing."
        )
        return

    send_notification(
        employee["name"],
        "Onboarding checks completed successfully."
    )


if __name__ == "__main__":
    onboard_employee("EMP001")