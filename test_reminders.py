import os


def test_json():
    """This method simply tests if the directory.json and reminders.json files are present in the project directory. If either file is missing, then the test fails.
    """
    assert os.path.isfile(".\\directory.json")
    assert os.path.isfile(".\\reminders.json")
