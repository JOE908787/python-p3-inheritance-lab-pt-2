#!/usr/bin/env python3

from student import Student, ChattyStudent

import io
import sys
import pytest

@pytest.mark.parametrize("student_class", [Student, ChattyStudent])
def test_student_methods(student_class):
    captured_out = io.StringIO()
    sys.stdout = captured_out
    student = student_class()
    student.hello()
    output = captured_out.getvalue().strip()
    assert output == ("Hello!" if student_class is Student else "Hello!\nBy the way, did you watch the latest episode of that show?")

    captured_out = io.StringIO()
    sys.stdout = captured_out
    student.raise_hand()
    output = captured_out.getvalue().strip()
    assert output == ("Raises hand respectfully." if student_class is Student else "Raises hand respectfully.\n" * 10).strip()
