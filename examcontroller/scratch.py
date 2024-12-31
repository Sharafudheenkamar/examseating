for i, seating in enumerate(classroom_seating):
    classroom_number = i + 1  # Classroom numbers start from 1
    for seat, subject in enumerate(seating):
        # Create a new SeatingArrangement object and save it to the database
        seating_entry = Seatingarrangement(classroom_number=classroom_number, seat_number=seat + 1,
                                           subject=subject, exam_date=exam_date)
        seating_entry.save()
