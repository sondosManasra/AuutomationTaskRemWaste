import pytest
from core.base_class import BaseClass


@pytest.mark.usefixtures("driver")
class UITest:

    @pytest.fixture(autouse=True)
    def setup_base(self, driver):
        self.base_class = BaseClass(driver)

    def test_valid_login(self):
        welcome_message = self.base_class.general_do_login()
        assert "Welcome" in welcome_message

    def test_login_add_update_delete_todos(self, driver):
        self.base_class.general_do_login()
        # Step 1: Add Todos
        todos = self.base_class.general_add_todos()
        assert "Learn Selenium" in todos
        assert "Write Pytest tests" in todos

        # Step 2: Update a Todo
        todos_after_update = self.base_class.general_uodate_todos()
        assert "Master Selenium" in todos_after_update
        assert "Learn Selenium" not in todos_after_update

        # Step 3: Delete a Todo
        todos_after_delete = self.base_class.general_delete_todos()
        assert "Write Pytest tests" not in todos_after_delete

    def test_invalid_login(self):
        alert_present = self.base_class.general_do_invalid_login()
        assert alert_present, "Expected alert for invalid login not found."
