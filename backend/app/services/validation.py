from app.schemas import SessionCreateRequest


def validate_session(payload: SessionCreateRequest) -> None:
    if payload.rep_count != len(payload.reps):
        raise ValueError(
            "rep_count must match the number of repetitions"
        )

    if payload.started_at >= payload.ended_at:
        raise ValueError(
            "started_at must be earlier than ended_at"
        )

    measured_duration = (
        payload.ended_at - payload.started_at
    ).total_seconds()

    if abs(payload.duration_seconds - measured_duration) > 2:
        raise ValueError(
            "duration_seconds does not match the timestamps"
        )

    expected_rep_numbers = list(
        range(1, payload.rep_count + 1)
    )

    actual_rep_numbers = [
        rep.rep_number for rep in payload.reps
    ]

    if actual_rep_numbers != expected_rep_numbers: #checks duplicate or missing rep number
        raise ValueError(
            "rep numbers must be sequential starting at 1"
        )

    valid_rep_numbers = set(actual_rep_numbers)

    for issue in payload.form_issues:
        if issue.rep_number not in valid_rep_numbers:
            raise ValueError(
                "a form issue references a missing repetition"
            )