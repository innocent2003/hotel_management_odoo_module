from odoo.tests import TransactionCase
from odoo.exceptions import AccessError, ValidationError

class TestSession7(TransactionCase):

    def setUp(self):
        super(TestSession7, self).setUp()
        # Create test data
        self.room = self.env['session7.hotel.room'].create({
            'name': 'Room 101',
            'price': 100.0,
            'is_available': True,
        })
        self.manager_group = self.env.ref('base.group_user')  # Assuming managers use base group
        self.staff_group = self.env.ref('base.group_user')  # Replace with actual staff group

    def test_room_creation(self):
        """Test room creation and field constraints."""
        room = self.env['session7.hotel.room'].create({
            'name': 'Room 102',
            'price': 200.0,
            'is_available': False,
        })
        self.assertEqual(room.name, 'Room 102', "Room name should be correctly set.")
        self.assertEqual(room.price, 200.0, "Room price should be correctly set.")
        self.assertFalse(room.is_available, "Room availability should be correctly set.")

        with self.assertRaises(ValidationError):
            self.env['session7.hotel.room'].create({
                'name': 'Room Invalid',
                'price': -50.0,
                'is_available': True,
            })

    def test_manager_access(self):
        """Test manager access rights."""
        self.env.user.groups_id |= self.manager_group
        self.room.sudo(self.env.user).write({'price': 150.0})
        self.assertEqual(self.room.price, 150.0, "Manager should be able to update the room price.")

    def test_staff_access(self):
        """Test staff access rights."""
        self.env.user.groups_id -= self.manager_group
        self.env.user.groups_id |= self.staff_group
        with self.assertRaises(AccessError):
            self.room.sudo(self.env.user).write({'price': 200.0})

    def test_get_room_details(self):
        """Test the `get_room_details` method."""
        details = self.room.get_room_details(self.room.id)
        self.assertEqual(details['name'], 'Room 101', "Room details should return correct name.")
        self.assertEqual(details['price'], 100.0, "Room details should return correct price.")
        self.assertTrue(details['is_available'], "Room details should return correct availability.")

    def test_logging_access_attempt(self):
        """Test custom logging for access attempts."""
        from ..utils.logging import log_access_attempt

        # Simulate successful access
        log_access_attempt(self.env.user.id, "session7.hotel.room", "read", True)
        # Simulate failed access
        log_access_attempt(self.env.user.id, "session7.hotel.room", "write", False)

        # Check log output manually or via mock logger (if extended).

